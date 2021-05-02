from django import forms
from .models import User, Newloan,LoanSummary, NewLoanImages, LoanackSummary, Sendmoney, SendmoneyImages

class loginuser(forms.Form):
  username = forms.CharField(max_length=64, label='username', 
     widget=forms.TextInput(attrs={'class': 'form-control','width':'40%'}))
  password = forms.CharField(label='password', 
     widget=forms.PasswordInput(attrs={'class': 'form-control','width':'40%'}))

Gender = [('MALE', 'Gender'),('MALE', 'MALE'),('FEMALE', 'FEMALE')]
Currency = [('CURRENCY', 'Currency'),('AED', 'AED'),('USD', 'USD')]
MERITAL = [('STATUS', 'STATUS'),('MARRIED', 'MARRIED'),('SINGLE', 'SINGLE'),('DEVORCED', 'DEVORCED')]

class NewLoanform(forms.ModelForm):
   class Meta:
       model = Newloan
       fields = ['status','firstname', 'lastname', 'passport', 'mobilenumber','gender', 'dateofbirth','zimidnumber','zimcontact','uaeaddress','referenceb', 
                  'uaeemployer', 'employercontact', 'nextofkin','kincontact','employeraddress','username','bankname','accnumber', 'country','branch','spaced','loanamount','confirmamount','amountwords','repperiod','loanpurpose','source','monthlyincome']
       labels = {'status':'Basic Information','firstname':'', 'lastname':'', 'passport':'', 'mobilenumber':'','gender':'', 'dateofbirth':'','zimidnumber':'','zimcontact':'','referenceb':'Employment and Next Of Kin!','uaeaddress':'', 
                 'uaeemployer':'', 'employercontact':'', 'nextofkin':'','kincontact':'','employeraddress':'','username':'Banking Details!','bankname':'','accnumber':'', 'country':'','branch':'','spaced':'Loan Details!','loanamount':'','confirmamount':'','amountwords':'','repperiod':'','loanpurpose':'','source':'','monthlyincome':''}
       widgets = {'status': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'firstname': forms.TextInput(attrs={'class':'border border-danger textforma','placeholder': 'Firstname'}),
                  'lastname' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Lastname'}), 
                  'passport' : forms.TextInput(attrs={'class': 'border border-danger textforma','placeholder': 'Passport Number'}),
                  'mobilenumber' : forms.NumberInput(attrs={'class': ' border border-danger textforma','placeholder': 'UAE Mobile Number'}),
                  'gender': forms.Select(choices = Gender, attrs={'class': 'border border-danger textforma', 'placeholder': 'Gender'}),
                  'dateofbirth' : forms.DateInput(attrs={'class':'border border-danger textforma', 'type': 'date', 'placeholder': 'Date Of Birth'}),
                  'zimidnumber':forms.TextInput(attrs={'class': 'border border-danger textforma','placeholder': 'Zim ID Number'}),
                  'zimcontact':forms.NumberInput(attrs={'class': 'border border-danger textforma','placeholder': 'Zim Contact Number'}),
                  'referenceb': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'uaeaddress' : forms.Textarea(attrs={'class': 'border border-danger textformb','placeholder': 'Current Physical Address in UAE', 'height':'18' }),
                  'uaeemployer' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'UAE Employer'}),
                  'employercontact' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Employer Contact'}),
                  'nextofkin' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Next Of Kin'}),
                  'kincontact' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Next Of Kin Contact'}),
                  'employeraddress' : forms.Textarea(attrs={'class': 'border border-danger textformb','placeholder': 'Employer Address',}),
                  'username': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'bankname': forms.TextInput(attrs={'class':'border border-danger textforma','placeholder': 'Bank Name'}),
                  'accnumber' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'IBAN/ACC Number'}), 
                  'country' : forms.TextInput(attrs={'class': 'border border-danger textforma','placeholder': 'Country'}),
                  'branch' : forms.TextInput(attrs={'class': 'border border-danger textforma','placeholder': 'Branch'}),
                  'spaced': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'loanamount' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Loan Amount'}),
                  'confirmamount' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Confirm Amount'}),
                  'amountwords' : forms.TextInput(attrs={'class':'border border-danger textformb', 'placeholder': 'Amount in Words'}),
                  'repperiod' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Repayment Period/Months'}),
                  'loanpurpose' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Purpose Of Loan'}),
                  'source' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Source Of Income'}),
                  'monthlyincome' : forms.NumberInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Monthly Income'}),
       }
  
class ImageForm(forms.ModelForm):
   class Meta:
       model = NewLoanImages
       fields =["images"]
       labels = {"images": "Upload Documents e.g id, passport, etc"}
       widgets = {'images':forms.FileInput(attrs={'class': 'custom-file','multiple': True,'id':'files'})}

class LoansummaryForm(forms.ModelForm):
   class Meta:
       model = LoanSummary
       fields =['fullname','pledged']
       labels = {'fullname':'','pledged':''}
       widgets = {'fullname' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'I.......(name)'}),
                  'pledged' : forms.TextInput(attrs={'class':'border border-danger textforma', 'placeholder': 'Have pledged my......(asset)'})
       }
class LoanackForm(forms.ModelForm):
   class Meta:
       model = LoanackSummary
       fields =['acknowledgement']
       labels = {'acknowledgement':''}
       widgets = {'acknowledgement' : forms.CheckboxInput(attrs={'class':'checkform', 'type' :'checkbox', 'id':'checkack'})
       }
    
class SendmoneyForm(forms.ModelForm):
   class Meta:
       model = Sendmoney
       fields = ['space','firstname', 'lastname','localidnumber','localcontact','currency','amount','uaeaddress', 
                 'referenceb','rfirstname', 'rlastname','rlocalidnumber','rlocalcontact','rcurrency', 'ramount','ruaeaddress', 'username','bankname','accnumber']
       labels = {'space':'Sender Details','firstname':'', 'lastname':'','localidnumber':'','localcontact':'','currency':'', 'amount':'','uaeaddress':'', 
                 'referenceb':'Receivers Details!','rfirstname':'', 'rlastname':'','rlocalidnumber':'','rlocalcontact':'','rcurrency':'','ramount':''
                 ,'ruaeaddress':'','username':'Receivers Bank Details!','bankname':'','accnumber':''}
       widgets = {'space': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'firstname': forms.TextInput(attrs={'class':'border border-primary textforma','placeholder': 'Firstname'}),
                  'lastname' : forms.TextInput(attrs={'class':'border border-primary textforma', 'placeholder': 'Lastname'}), 
                  'localidnumber':forms.TextInput(attrs={'class': 'border border-primary textforma','placeholder': 'Local ID number/Passport Number'}),
                  'localcontact':forms.NumberInput(attrs={'class': 'border border-primary textforma','placeholder': 'Local Contact Number'}),
                  'currency': forms.Select(choices = Currency, attrs={'class': 'border border-primary textforma', 'placeholder': 'Currency', 'id':'currency'}),
                  'amount' : forms.NumberInput(attrs={'class':'border border-primary textforma', 'placeholder': 'Amount', 'id':'amount'}),
                  'uaeaddress' : forms.Textarea(attrs={'class': 'border border-primary textformb','placeholder': 'Senders current Physical Address', 'height':'18' }),
                  'referenceb': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}), 
                  'rfirstname': forms.TextInput(attrs={'class':'border border-primary textforma','placeholder': 'Firstname'}),
                  'rlastname' : forms.TextInput(attrs={'class':'border border-primary textforma', 'placeholder': 'Lastname'}), 
                  'rlocalidnumber':forms.TextInput(attrs={'class': 'border border-primary textforma','placeholder': 'Local ID number/Passport Number'}),
                  'rlocalcontact':forms.NumberInput(attrs={'class': 'border border-primary textforma','placeholder': 'Local Contact Number'}),
                  'rcurrency' : forms.TextInput(attrs={'class':'border border-primary textforma', 'placeholder': 'Currency', 'id':'rcurrency', 'disabled':'True'}),
                  'ramount' : forms.NumberInput(attrs={'class':'border border-primary textforma', 'placeholder': 'Amount', 'id':'ramount', 'disabled':'True'}),
                  'ruaeaddress' : forms.Textarea(attrs={'class': 'border border-primary textformb','placeholder': 'Receivers current Physical Address', 'height':'18' }),
                  'username': forms.TextInput(attrs={'class':'spacefield', 'autocomplete':'off', 'disabled':'True'}),
                  'bankname': forms.TextInput(attrs={'class':'border border-primary textforma','placeholder': 'Bank Name'}),
                  'accnumber' : forms.TextInput(attrs={'class':'border border-primary textforma', 'placeholder': 'IBAN/ACC Number'}),         
       }
    
class SendImageForm(forms.ModelForm):
   class Meta:
       model = SendmoneyImages
       fields =["images"]
       labels = {"images": "Upload Documents"}
       widgets = {'images':forms.FileInput(attrs={'class': 'custom-file','multiple': True,'id':'files'})}