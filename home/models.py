from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Newloan(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  passport = models.CharField(max_length=15)
  mobilenumber = models.IntegerField()
  gender = models.CharField(max_length=10)
  dateofbirth = models.DateField(max_length=10)
  zimidnumber = models.CharField(max_length=50)
  zimcontact = models.IntegerField()
  uaeaddress = models.TextField(max_length=1000)
  uaeemployer = models.CharField(max_length=50)
  employercontact = models.IntegerField()
  nextofkin = models.CharField(max_length=50)
  kincontact = models.IntegerField()
  employeraddress = models.TextField(max_length=1000)
  bankname = models.CharField(max_length=50, blank=True)
  accnumber = models.CharField(max_length=50, blank=True, null=True)
  country = models.CharField(max_length=50, blank=True, null=True)
  branch = models.CharField(max_length=50, blank=True, null=True)
  loanamount = models.IntegerField()
  confirmamount = models.IntegerField()
  amountwords = models.CharField(max_length=50)
  repperiod = models.IntegerField()
  loanpurpose = models.CharField(max_length=50)
  source = models.CharField(max_length=50)
  monthlyincome = models.IntegerField()
  status = models.CharField(max_length=50, blank=True)
  referenceb = models.CharField(max_length=50, blank=True)
  username = models.CharField(max_length=50, blank=True)
  spaced = models.CharField(max_length=50, blank=True)

  def serialize(self):
        return {
            "id": self.id, 'firstname': self.firstname, 'lastname':self.lastname, 'passport':self.passport, 
            'mobilenumber':self.mobilenumber,'gender': self.gender, 'dateofbirth':self.dateofbirth,'zimidnumber':self.zimidnumber,
            'zimcontact':self.zimcontact, 'uaeaddress':self.uaeaddress,'uaeemployer':self.uaeemployer, 'employercontact':self.employercontact,
            'nextofkin':self.nextofkin, 'kincontact':self.kincontact,'employeraddress':self.employeraddress, 'bankname':self.bankname,
            'accnumber':self.accnumber, 'country':self.country,'branch':self.branch, 'loanamount':self.loanamount,
            'confirmamount':self.confirmamount,'repperiod':self.repperiod,'loanpurpose':self.loanpurpose,'source':self.source,'monthlyincome':self.monthlyincome
            }
  def __str__(self): 
      return f"{self.username}"

class LoanSummary(models.Model):
  fullname = models.CharField(max_length=50)
  pledged = models.CharField(max_length=50)
  acknowledgement = models.BooleanField(default=False)
  def serialize(self):
        return {
            "id": self.id, 'firstname': self.firstname, 'lastname':self.lastname
            }
  def __str__(self): 
      return f"{self.fullname}"

class LoanackSummary(models.Model):
   acknowledgement = models.BooleanField(default=False)
   def serialize(self):
        return {"id": self.id, 'acknowledgement': self.acknowledgement}

class NewLoanImages(models.Model):
  entry = models.ForeignKey(Newloan, default=None, on_delete=models.CASCADE, related_name="photoset")
  images = models.FileField(upload_to='newloanimage', verbose_name='Image', max_length=254)
  def __str__(self): 
      return f"{self.entry.username}"            

class Sendmoney(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  localcontact = models.IntegerField()
  localidnumber = models.CharField(max_length=50)
  currency = models.CharField(max_length=10)
  amount = models.FloatField()
  uaeaddress = models.TextField(max_length=1000)
  rfirstname = models.CharField(max_length=50)
  rlastname = models.CharField(max_length=50)
  rlocalcontact = models.IntegerField()
  rlocalidnumber = models.CharField(max_length=50)
  rcurrency = models.CharField(max_length=10, blank=True)
  ramount = models.FloatField(blank=True)
  ruaeaddress = models.TextField(max_length=1000)
  bankname = models.CharField(max_length=50, blank=True)
  accnumber = models.CharField(max_length=50, blank=True)
  space = models.CharField(max_length=50, blank=True)
  referenceb = models.CharField(max_length=50, blank=True)
  username = models.CharField(max_length=50, blank=True)

  def serialize(self):
        return {
            "id": self.id, 'firstname': self.firstname, 'lastname':self.lastname, 'passport':self.passport, 
            'mobilenumber':self.mobilenumber,'zimidnumber':self.zimidnumber,
            'zimcontact':self.zimcontact, 'uaeaddress':self.uaeaddress,'bankname':self.bankname,
            'accnumber':self.accnumber,'loanamount':self.loanamount, 'confirmamount':self.confirmamount,
            }
  def __str__(self):
        return f"{self.username}"

class SendmoneyImages(models.Model):
  entry = models.ForeignKey(Sendmoney, default=None, on_delete=models.CASCADE, related_name="photoset")
  images = models.FileField(upload_to='newloanimage', verbose_name='Image', max_length=254)
  def __str__(self): 
      return f"{self.entry.username}"