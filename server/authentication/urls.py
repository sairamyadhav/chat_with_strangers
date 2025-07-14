from django.urls import path
from .views import SignIn, GuestSignin, Login

urlpatterns = [
    path("signin", SignIn.as_view(), name="signin"),
    path("guest_signin", GuestSignin.as_view(), name="guest_signin"),
    path("login", Login.as_view(), name="login"),
]
