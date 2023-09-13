from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .constants import Role
from .models import (
    User,
    Seller,
    Customer,
    DeliveryDriver,
    Administrator,
    AffiliateMarketer,
    CustomerServiceRepresentative,
    MarketingManager,
    ProductManager,
    SocialMediaInfluencer,
    SalesRepresentative,
    LogisticsCoordinator,
    FinancialAnalyst,
    DataAnalyst,
    LegalCounsel,
    InventoryManager,
)
from .forms import (
    SellerAdminForm,
    CustomerAdminForm,
    DeliveryDriverAdminForm,
    AdministratorAdminForm,
    AffiliateMarketerAdminForm,
    CustomerServiceRepresentativeAdminForm,
    MarketingManagerAdminForm,
    ProductManagerAdminForm,
    SocialMediaInfluencerAdminForm,
    SalesRepresentativeAdminForm,
    LogisticsCoordinatorAdminForm,
    FinancialAnalystAdminForm,
    DataAnalystAdminForm,
    LegalCounselAdminForm,
    InventoryManagerAdminForm,
)
from .admin_extras import generate_fieldsets, UserMixin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        "name",
        "email",
        "phone",
        "bank_name",
        "bank_account_number",
        "payment_preferences",
        "is_staff",
        "is_active",
        "is_superuser",
        "role",
        "last_login",
        "date_joined",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
    )

    raw_id_fields = ("groups", "user_permissions")
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
class SellerAdmin(UserMixin):
    list_display = (
        "user",
        "company_name",
        "business_registration_number",
        "tax_identification_number",
        "business_type",
    )
    list_filter = ("company_name", "business_type")
    form = SellerAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Business", "Payment", "Permissions"],
    )


@admin.register(Customer)
class CustomerAdmin(UserMixin):
    form = CustomerAdminForm
    list_display = (
        "user",
        "shipping_address",
        "billing_address",
        "email_subscription",
    )
    list_filter = ("email_subscription",)
    raw_id_fields = ("wishlist",)

    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Shipping And Billing Info",
            "Payment",
            "Permissions",
        ],
    )


@admin.register(DeliveryDriver)
class DeliveryAdmin(UserMixin):
    form = DeliveryDriverAdminForm
    list_display = (
        "user",
        "license_number",
        "vehicle_type",
        "vehicle_registration_number",
    )
    list_filter = ("vehicle_type",)
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Driver Info",
            "Payment",
            "Permissions",
        ],
    )


@admin.register(Administrator)
class AdministratorAdmin(UserMixin):
    form = AdministratorAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment"],
    )


@admin.register(AffiliateMarketer)
class AffiliateMarketerAdmin(UserMixin):
    form = AffiliateMarketerAdminForm
    list_display = ("user", "marketing_campaign")
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Affiliate Marketer"],
    )
    role = Role.AFFILIATE_MARKETER


@admin.register(CustomerServiceRepresentative)
class CustomerServiceRepresentativeAdmin(UserMixin):
    form = CustomerServiceRepresentativeAdminForm
    list_display = (
        "user",
        "department",
        "support_ticket_assignments",
        "performance_metrics",
    )
    list_filter = ("department",)

    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Permissions",
            "Customer Service Staff Representative",
        ],
    )


@admin.register(MarketingManager)
class MarketingManagerAdmin(UserMixin):
    form = MarketingManagerAdminForm
    list_display = (
        "user",
        "marketing_campaigns",
        "marketing_budget",
        "marketing_strategy",
    )
    list_filter = ("marketing_campaigns", "marketing_strategy")
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Permissions",
            "Marketing Info",
        ],
    )


@admin.register(ProductManager)
class ProductManagerAdmin(UserMixin):
    form = ProductManagerAdminForm
    list_display = (
        "user",
        "product_categories",
        "product_SKUs",
        "product_descriptions",
    )
    list_filter = ("product_categories",)
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Product Info"],
    )


@admin.register(SocialMediaInfluencer)
class SocialMediaInfluencerAdmin(UserMixin):
    form = SocialMediaInfluencerAdminForm
    list_display = (
        "user",
        "social_media_profiles",
        "follower_count",
        "engagement_metrics",
        "content_type",
    )
    list_filter = ("social_media_profiles", "content_type")
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Social Info"],
    )


@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(UserMixin):
    form = SalesRepresentativeAdminForm
    list_display = ("user", "sales_targets")
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Sales infos"],
    )


@admin.register(LogisticsCoordinator)
class LogisticsCoordinatorAdmin(UserMixin):
    form = LogisticsCoordinatorAdminForm
    list_display = (
        "user",
        "shipping_methods",
        "tracking_information",
        "delivery_schedules",
    )
    list_filter = ("shipping_methods",)
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Logistics Info"],
    )


@admin.register(LegalCounsel)
class LegalCounselAdmin(UserMixin):
    form = LegalCounselAdminForm
    list_display = ("user", "legal_documents", "legal_cases", "legal_advice")
    list_filter = ("legal_cases",)
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Permissions",
        ],
    )


@admin.register(InventoryManager)
class InventoryManagerAdmin(UserMixin):
    form = InventoryManagerAdminForm
    list_display = ("user", "inventory_tracking_data")
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Permissions",
        ],
    )


@admin.register(FinancialAnalyst)
class FinancialAnalystAdmin(UserMixin):
    form = FinancialAnalystAdminForm
    list_display = (
        "user",
        "financial_data",
        "reports",
        "forecasting_models",
    )
    list_filter = ("financial_data",)
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Financial Info",
            "Permissions",
        ],
    )


@admin.register(DataAnalyst)
class DataAnalystAdmin(UserMixin):
    form = DataAnalystAdminForm
    list_display = (
        "user",
        "data_sources",
        "analysis_methodologies",
        "reports_generated",
    )
    list_filter = ("data_sources", "analysis_methodologies")
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Data Analyst Info",
            "Permissions",
        ],
    )
