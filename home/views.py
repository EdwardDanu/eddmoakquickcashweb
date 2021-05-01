from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from .models import User, Newloan, LoanSummary, NewLoanImages, LoanackSummary, Sendmoney, SendmoneyImages
from .forms import loginuser, ImageForm, NewLoanform, LoansummaryForm, LoanackForm,SendmoneyForm,SendImageForm
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "home/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "home/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "home/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "home/login.html", {
              "form":loginuser,
              "message": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html", {
        "form":loginuser })


def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse("index"))

#home index
def index(request):
  return render(request, "home/index.html")

@login_required(login_url='login')
def newloan(request):
    args = {}
    if request.method == "POST":
        form = NewLoanform(request.POST)
        formset = request.FILES.getlist('images')
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.loanamount != instance.confirmamount:
                form = NewLoanform()
                args['form'] = form
                return render(request, "home/newloan.html", {
                'forms': NewLoanform(),
                'formset': ImageForm(),
                'message': "Please confirm Amount"})
            for image in formset:
                mainpost = NewLoanImages(entry=instance, images=image)
                instance.status = "Loan Application Submitted"
                instance.save()
                reference = instance.id
                related_reference = f"LO{instance.firstname[0:3].upper()}{reference * 2}"
                instance.referenceb = related_reference
                instance.username = request.user.username
                amount = float(instance.loanamount)
                interest = float(0.10) * amount
                total_amount = amount + interest
                amount_in_words = instance.amountwords
                mainpost.save()
                instance.save()
            return render(request, "home/loansummary.html", {
                'amount': amount,
                'interest': interest,
                'total_amount': total_amount,
                'amount_in_words': amount_in_words,
                'LoansummaryForm':LoansummaryForm(),
                'LoanackForm':LoanackForm(),
                'related_reference':related_reference
                })
        else:
            form = NewLoanform()
            args['form'] = form
            return render(request, "home/newloan.html", {
            'forms': NewLoanform(),
            'formset': ImageForm(),
            'message': "please complete all fields properly"})
    else:
        return render(request, "home/newloan.html",{
            'forms': NewLoanform(),
            'formset' : ImageForm()
        })

def loansummary(request):
     if request.method == "POST":
         loansummary = LoansummaryForm(request.POST)
         loanack =LoanackForm(request.POST)
         amount_in_words = request.POST["amount_in_words"]
         amount = float(request.POST["amount"])
         ref = int(request.POST["reference"])
         if loansummary.is_valid() and loanack.is_valid():
             acknowledgement = loanack.cleaned_data["acknowledgement"]
             if acknowledgement == True:
                 loansummary.save()
                 loanack.save()
                 entry = Newloan.objects.get(pk=ref)
                 amount = entry.loanamount
                 interest = float(0.10) * amount
                 total_amount = amount + interest
                 amount_in_words = entry.amountwords
                 status = entry.status
                 referenceb = entry.referenceb
                 return render(request, "home/loanstatussummary.html", {
                'amount': amount,
                'interest': interest,
                'total_amount': total_amount,
                'amount_in_words': amount_in_words,
                'status':status,
                'referenceb':referenceb
                })
             else:
                 interest = 0.10 * amount
                 return render(request, "home/loansummary.html",{
                 'amount': amount,
                 'interest' : interest,
                 'total_amount': amount + interest,
                 'amount_in_words': amount_in_words,
                 'LoansummaryForm' : loansummary,
                 'LoanackForm': loanack,
                 'referenceb':referenceb,
                 'message': "Agree to terms and conditions"
                 })
@login_required(login_url='login')
def sendmoney(request):
     args = {}
     if request.method == "POST":
        form = SendmoneyForm(request.POST)
        formset = request.FILES.getlist('images')
        if form.is_valid():
            instance = form.save(commit=False)
            for image in formset:
                sendimages = SendmoneyImages(entry=instance, images=image)
                instance.space = "Transaction Inprocess"
                if instance.currency == "AED":
                    instance.rcurrency = "USD"
                    instance.ramount = instance.amount / 3.66
                else:
                    instance.rcurrency = "AED"
                    instance.ramount = instance.amount * 3.66
                instance.save() 
                ref = instance.id
                related_reference = f"TR{instance.firstname[0:3].upper()}{ref * 2}"
                instance.referenceb = related_reference
                instance.username = request.user.username
                instance.save()
                sendimages.save()
                return HttpResponseRedirect(reverse("sendsummary", kwargs={'name': related_reference }))
        else:
            form = SendmoneyForm()
            args['form'] = form
            return render(request, "home/sendmoney.html",{
            'forms': SendmoneyForm(),
            'formset' : SendImageForm(),
            'message': "please complete all fields properly"
            })
     else:
         return render(request, "home/sendmoney.html",{
            'forms': SendmoneyForm(),
            'formset' : SendImageForm()
        })
def sendsummary(request, name):
     if request.method == "POST":
         pass
     else:
         try:
             entry = Sendmoney.objects.filter(referenceb=name).first()
             if entry.username == request.user.username:
                 sender_firstname = entry.firstname
                 sender_lastname = entry.lastname
                 sender_contact = entry.localcontact
                 sender_currency = entry.currency
                 sender_amount = entry.amount
                 receiver_firstname = entry.rfirstname
                 receiver_lastname = entry.rlastname
                 receiver_contact = entry.rlocalcontact
                 receiver_currency = entry.rcurrency
                 receiver_amount = entry.ramount
                 status = entry.space
                 return render(request, "home/sendsummary.html",{
                 'reference':name,
                 'sender_firstname': sender_firstname.capitalize(),
                 'sender_lastname': sender_lastname.capitalize(),
                 'sender_contact': sender_contact,
                 'sender_currency' : sender_currency,
                 'sender_amount' : sender_amount,
                 'receiver_firstname' : receiver_firstname.capitalize(),
                 'receiver_lastname' : receiver_lastname.capitalize(),
                 'receiver_contact': receiver_contact,
                 'receiver_currency': receiver_currency,
                 'receiver_amount' : receiver_amount,
                 'status': status
                        }) 
             else:
                 return render(request, "home/transferstatus.html", {
                 "message": "User not authorised to view this transaction"
            })
         except AttributeError:
             return render(request, "home/transferstatus.html", {
                "message": "Wrong Reference number!!"
            })
@login_required(login_url='login')
def transferstatus(request):
    if request.method == "POST":
        ref = request.POST["referenceb"]
        return HttpResponseRedirect(reverse("sendsummary", kwargs={'name': ref }))
    else:
         return render(request, "home/transferstatus.html", {
            }) 
@login_required(login_url='login')
def loanstatus(request):
    if request.method == "POST":
         ref = request.POST["referenceb"]
         try:
             entry = Newloan.objects.filter(referenceb=ref).first()
             if entry.username == request.user.username:
                 amount = entry.loanamount
                 interest = float(0.10) * amount
                 total_amount = amount + interest
                 amount_in_words = entry.amountwords
                 status = entry.status
                 return render(request, "home/loanstatussummary.html", {
                    'amount': amount,
                    'interest': interest,
                    'total_amount': total_amount,
                    'amount_in_words': amount_in_words,
                    'status':status,
                    'referenceb':ref
                    })
             else:
                 return render(request, "home/loanstatus.html", {
                 "message": "User not authorised to view this transaction!!"
            })
         except AttributeError:
             return render(request, "home/loanstatus.html", {
                "message": "Wrong Reference number!!"
            })
    else:
         return render(request, "home/loanstatus.html")