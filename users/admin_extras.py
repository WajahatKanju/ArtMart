from .constants import Role
from typing import Any
from .models import User


class UserMixin:
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]

        is_staff = form.cleaned_data["is_staff"]
        is_active = form.cleaned_data["is_active"]

        bank_name = form.cleaned_data["bank_name"]
        bank_account_number = form.cleaned_data["bank_account_number"]
        payment_preferences = form.cleaned_data["payment_preferences"]

        if hasattr(self, "role"):
            role = self.role
        else:
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


def generate_fieldsets(include_parts=None):
    parts = {
        "Personal Info": (
            ("first_name", "last_name"),
            "email",
            ("password1", "password2"),
            "phone",
        ),
        "Business": (
            "company_name",
            "business_registration_number",
            "tax_identification_number",
            "business_type",
        ),
        "Shipping And Billing Info": (
            "shipping_address",
            "billing_address",
        ),
        "Payment": ("bank_name", "bank_account_number", "payment_preferences"),
        "Driver Info": (
            "license_number",
            "vehicle_type",
            "vehicle_registration_number",
        ),
        "Affiliate Marketer": ("marketing_campaign",),
        "Customer Service Staff Representative": (
            "department",
            "support_ticket_assignments",
            "performance_metrics",
        ),
        "Marketing Info": ("marketing_campaigns", "marketing_strategy"),
        "Product Info": ("product_categories", "product_SKUs", "product_descriptions"),
        "Social Info": (
            "social_media_profiles",
            "follower_count",
            "engagement_metrics",
            "content_type",
        ),
        "Sales info": ("sales_targets",),
        "Logistics Info": (
            "shipping_methods",
            "tracking_information",
            "delivery_schedules",
        ),
        "Financial Info": ("dinancial_data", "reports", "forecasting_models"),
        "Data Analyst Info": (
            "data_sources",
            "analysis_methodologies",
            "reports_generated",
        ),
        "Legal Info": ("legal_documents", "legal_cases", "legal_advice"),
        "Inventory": ("inventory_tracking_data"),
        "Permissions": ("is_staff", "is_active"),
    }

    if include_parts:
        fieldsets = [
            (part_name, {"fields": part_fields})
            for part_name, part_fields in parts.items()
            if part_name in include_parts
        ]
    else:
        fieldsets = list(parts.items())

    return fieldsets
