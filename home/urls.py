from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newloan", views.newloan, name="newloan"),
    path("newloan/summary", views.loansummary, name="loansummary"),
    path("loanstatus", views.loanstatus, name="loanstatus"),
    path("sendmoney", views.sendmoney, name="sendmoney"),
    path("transferstatus", views.transferstatus, name="transferstatus"),
    path("sendsummary/<str:name>", views.sendsummary, name="sendsummary")
]