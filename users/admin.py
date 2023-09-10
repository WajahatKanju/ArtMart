from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Seller, Customer


class SellerInline(admin.StackedInline):
    model = Seller
    extra = 1


class CustomerInline(admin.StackedInline):
    model = Customer
    extra = 1


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


admin.site.register(Seller)
admin.site.register(Customer)


# @admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass
    # list_display = (
    #     "company_name",
    #     "business_registration_number",
    #     "tax_identification_number",
    #     "business_type",
    #     # Add other fields you want to display in the list view
    # )

    # form = SellerAdminForm  # Use the custom form for the Seller model
    # fields = [
    #     # List all fields you want in the form except 'user'
    #     "company_name",
    #     "business_registration_number",
    #     "tax_identification_number",
    #     "business_type",
    #     "first_name",
    #     "last_name",
    #     "email",
    #     "is_staff",
    #     "is_active",
    #     "bank_name",
    #     "bank_account_number",
    #     "payment_preferences",
    #     "password",
    #     "password_confirm",
    #     # Add other fields as needed
    # ]
    # # Customize any other admin options as needed
