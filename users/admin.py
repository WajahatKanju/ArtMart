from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Seller


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
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
                    "email",
                    ("first_name", "last_name"),
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
                    "company_name",
                    "business_registration_number",
                    "tax_identification_number",
                    "business_type",
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
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                    "phone",
                    "bank_name",
                    "bank_account_number",
                    "payment_preferences",
                    "company_name",
                    "business_registration_number",
                    "tax_identification_number",
                    "business_type",
                    "role",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Seller)
class SellerAdmin(UserAdmin):
    model = Seller

    list_display = ("name", "date_joined", "last_login")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    ("first_name", "last_name"),
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    ordering = ("email",)

    def name(self, obj):
        print(obj)
        return f"{obj.first_name} {obj.last_name}"
