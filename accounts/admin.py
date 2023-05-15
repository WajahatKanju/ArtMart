from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.hashers import make_password

from .models import User, Address


class UserAdmin(BaseUserAdmin):
    def save_model(self, request, obj, form, change):
        # Check if the password has changed
        if change and "password" in form.changed_data:
            # Set the password to the hashed value
            obj.password = make_password(form.cleaned_data["password"])

        super().save_model(request, obj, form, change)


admin.site.register(Address)
admin.site.register(User, UserAdmin)
