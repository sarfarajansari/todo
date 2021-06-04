from django.contrib.auth import login
from django.urls import path
from .import views

urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("otp/",views.otpapi,name="otp"),
    path("test/",views.check,name="test"),
]