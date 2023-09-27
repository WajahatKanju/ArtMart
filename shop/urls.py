from django.urls import path

from .views import handler_404
from .views import Index, Register, UserLogin, AboutView, ContactView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("register/", Register.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("404/", handler_404, name="not_found"),
]
