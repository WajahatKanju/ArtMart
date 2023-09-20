from django.urls import path

from .views import index, register, user_login, handler_404

urlpatterns = [
    path("", index),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("404/", handler_404, name="not_found"),
]
