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
class SellerAdmin(UserMixin):
    form = SellerAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Business", "Payment", "Permissions"],
    )


@admin.register(Customer)
class CustomerAdmin(UserMixin):
    form = CustomerAdminForm
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
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Affiliate Marketer"],
    )
    role = Role.AFFILIATE_MARKETER


@admin.register(CustomerServiceRepresentative)
class CustomerServiceRepresentativeAdmin(UserMixin):
    form = CustomerServiceRepresentativeAdminForm
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
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Product Info"],
    )


@admin.register(SocialMediaInfluencer)
class SocialMediaInfluencerAdmin(UserMixin):
    form = SocialMediaInfluencerAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Social Info"],
    )


@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(UserMixin):
    form = SalesRepresentativeAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Sales infos"],
    )


@admin.register(LogisticsCoordinator)
class LogisticsCoordinatorAdmin(UserMixin):
    form = LogisticsCoordinatorAdminForm
    fieldsets = generate_fieldsets(
        include_parts=["Personal Info", "Payment", "Permissions", "Logistics Info"],
    )


@admin.register(LegalCounsel)
class LegalCounselAdmin(UserMixin):
    form = LegalCounselAdminForm
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
    fieldsets = generate_fieldsets(
        include_parts=[
            "Personal Info",
            "Payment",
            "Data Analyst Info",
            "Permissions",
        ],
    )
