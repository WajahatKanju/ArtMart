from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import login, authenticate
from .forms import CustomerSignInForm, UserLoginForm
from users.models import User
from users.constants import Role


class BaseView(View):
    site_name = "Artmart"
    site_mail = "artmartswat@gmail.com"

    def render_template(self, request, template_name, context={}):
        context["site_name"] = self.site_name
        context["site_mail"] = self.site_mail
        return render(request, template_name, context)


class Index(BaseView):
    def get(self, request):
        return self.render_template(request, "shop/index.html")


class Register(BaseView):
    def get(self, request):
        form = CustomerSignInForm()

        return self.render_template(
            request, "authentication/register.html", {"form": form}
        )

    def post(self, request):
        form = CustomerSignInForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]

            bank_name = form.cleaned_data["bank_name"]
            bank_account_number = form.cleaned_data["bank_account_number"]
            payment_preferences = form.cleaned_data["payment_preferences"]

            user, _ = User.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                is_staff=False,
                is_active=True,
                bank_name=bank_name,
                bank_account_number=bank_account_number,
                payment_preferences=payment_preferences,
                role=Role.CUSTOMER,
            )
            print("A User Was Created / Retrived ", user)
            form.save(user)

            login(request, user)
            return redirect("home")  # Redirect to your desired page after registration
        return self.render_template(
            request, "authentication/register.html", {"form": form}
        )


class UserLogin(BaseView):
    def get(self, request):
        form = UserLoginForm()
        return self.render_template(
            request, "authentication/login.html", {"form": form}
        )

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            print("________________________")
            print("________________________")
            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")

            login(request, user)
            return redirect("index")  # Redirect to your desired page after login
        else:
            print("Error Above Me")
        return self.render_template(
            request, "authentication/login.html", {"form": form}
        )


class AboutView(BaseView):
    def get(self, request):
        return self.render_template(request, "shop/about.html")


class ContactView(BaseView):
    def get(self, request):
        return self.render_template(request, "shop/contact.html")


def handler_404(request, *args, **kwargs):
    return render(request, "shop/404.html", status=404)
