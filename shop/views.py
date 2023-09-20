from django.shortcuts import render, redirect
from products.models import Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {"categories": categories, "brand_name": "Artmart"}
    return render(request, "shop/index.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")  # Redirect to your desired page after registration
    else:
        form = UserCreationForm()
    return render(request, "authentication/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")  # Redirect to your desired page after login
    else:
        form = AuthenticationForm()
    return render(request, "authentication/login.html", {"form": form})


def handler_404(request, *args, **kwargs):
    return render(request, "shop/404.html", status=404)
