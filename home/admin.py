from django.contrib import admin
from .models import Newloan, NewLoanImages, LoanSummary, LoanackSummary, Sendmoney,SendmoneyImages

#Register your models here.
admin.site.register(Newloan)
admin.site.register(NewLoanImages)
admin.site.register(LoanSummary)
admin.site.register(LoanackSummary)
admin.site.register(Sendmoney)
admin.site.register(SendmoneyImages)
