from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Seller, Customer
from .forms import SellerAdminForm
from .constants import Role


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("first_name", "last_name"),
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "phone",
                    "bank_name",
                    "bank_account_number",
                    "payment_preferences",
                ),
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        (
            "Roles",
            {"fields": ("role",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    ("first_name", "last_name"),
                    "email",
                    "password1",
                    "password2",
                    "phone",
                    "bank_name",
                    "bank_account_number",
                    "payment_preferences",
                ),
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    form = SellerAdminForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "first_name",
                        "last_name",
                    ),
                    "email",
                    ("password1", "password2"),
                    "phone",
                )
            },
        ),
        (
            "Business",
            {
                "fields": (
                    "company_name",
                    "business_registration_number",
                    "tax_identification_number",
                    "business_type",
                )
            },
        ),
        (
            "Payment",
            {
                "fields": (
                    "bank_name",
                    "bank_account_number",
                    "payment_preferences",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]

        is_staff = form.cleaned_data["is_staff"]
        is_active = form.cleaned_data["is_active"]

        bank_name = form.cleaned_data["bank_name"]
        bank_account_number = form.cleaned_data["bank_account_number"]
        payment_preferences = form.cleaned_data["payment_preferences"]
        role = Role.SELLER

        user, _ = User.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            is_staff=is_staff,
            is_active=is_active,
            bank_name=bank_name,
            bank_account_number=bank_account_number,
            payment_preferences=payment_preferences,
            role=role,
        )
        obj.user = user
        return super().save_model(request, obj, form, change)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = SellerAdminForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "first_name",
                        "last_name",
                    ),
                    "email",
                    ("password1", "password2"),
                    "phone",
                )
            },
        ),
        (
            "Shipping And Billing Info",
            {
                "fields": (
                    "shipping_address",
                    "billing_address",
                )
            },
        ),
        (
            "Payment",
            {
                "fields": (
                    "bank_name",
                    "bank_account_number",
                    "payment_preferences",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active",)},
        ),
    )

    def save_model(self, request, obj, form, change):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]

        is_staff = False
        is_active = form.cleaned_data["is_active"]

        bank_name = form.cleaned_data["bank_name"]
        bank_account_number = form.cleaned_data["bank_account_number"]
        payment_preferences = form.cleaned_data["payment_preferences"]
        role = Role.CUSTOMER

        user, _ = User.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            is_staff=is_staff,
            is_active=is_active,
            bank_name=bank_name,
            bank_account_number=bank_account_number,
            payment_preferences=payment_preferences,
            role=role,
        )
        obj.user = user
        return super().save_model(request, obj, form, change)
