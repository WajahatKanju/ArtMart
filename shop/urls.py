from django.urls import path
from .views import index, register, user_login

urlpatterns = [
    path("", index),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
]
