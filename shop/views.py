from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login


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
        form = UserCreationForm()
        return self.render_template(
            request, "authentication/register.html", {"form": form}
        )

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")  # Redirect to your desired page after registration
        return self.render_template(
            request, "authentication/register.html", {"form": form}
        )


class UserLogin(BaseView):
    def get(self, request):
        form = AuthenticationForm()
        return self.render_template(
            request, "authentication/login.html", {"form": form}
        )

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")  # Redirect to your desired page after login
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
