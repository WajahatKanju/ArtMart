from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .constants import Role, PaymentPreference, BUSINESS_TYPES


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        _("first name"),
        max_length=50,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=50,
    )
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    bank_name = models.CharField(_("Bank Name"), max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(
        _("Bank Account Number"), max_length=50, blank=True, null=True
    )
    payment_preferences = models.CharField(
        _("Payment Preferences"),
        max_length=50,
        choices=PaymentPreference.choices,
        blank=True,
        null=True,
    )

    role = models.CharField(max_length=50, choices=Role.choices)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    phone = models.CharField(max_length=11)
    # Custom Fields

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email} "

    def name(self) -> str:
        if len(self.first_name + self.last_name) > 0:
            return self.first_name + self.last_name
        return "UNDEFINED"


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(_("Company Name"), max_length=75)
    business_registration_number = models.CharField(
        _("Business Registration Number"), max_length=50
    )
    tax_identification_number = models.CharField(
        _("Tax Identification Number (TIN)"), max_length=50
    )
    business_type = models.CharField(
        _("Business Type"), max_length=50, choices=BUSINESS_TYPES.choices
    )

    def __str__(self):
        return self.company_name

    def number_of_products(self) -> int:
        return self.products.count()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Additional Customer Information
    shipping_address = models.TextField(_("Shipping Address"), blank=True, null=True)
    billing_address = models.TextField(_("Billing Address"), blank=True, null=True)

    wishlist = models.ManyToManyField(
        "products.Product", verbose_name=_("Wishlist"), blank=True
    )

    # Customer Preferences
    email_subscription = models.BooleanField(
        _("Email Subscription"),
        default=True,
        help_text=_("Subscribe to email updates and newsletters."),
    )

    def __str__(self) -> str:
        return f"Customer: {self.user.email}"


class DeliveryDriver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    license_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    vehicle_registration_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Delivery Driver")
        verbose_name_plural = _("Delivery Drivers")

    def __str__(self) -> str:
        return self.user.email


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = _("Administrator")
        verbose_name_plural = _("Administrators")

    def __str__(self) -> str:
        return self.user.email


class AffiliateMarketer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    marketing_campaign = models.CharField(max_length=100, blank=True, null=True)
    base_role = Role.AFFILIATE_MARKETER

    class Meta:
        verbose_name = _("Affiliate Marketer")
        verbose_name_plural = _("Affiliate Marketers")

    def __str__(self) -> str:
        return self.user.email


class CustomerServiceRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    # ? support_ticket_assignments = models.ManyToManyField("SupportTicket", blank=True)
    support_ticket_assignments = models.TextField(blank=True)
    performance_metrics = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name = _("Customer Service")
        verbose_name_plural = _("Customer Service")

    def __str__(self) -> str:
        return self.user.email


class MarketingManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # ? marketing_campaigns = models.ManyToManyField("MarketingCampaign", blank=True)
    marketing_campaigns = models.TextField(blank=True)
    marketing_budget = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    marketing_strategy = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Marketing Manager")
        verbose_name_plural = _("Marketing Managers")

    def __str__(self) -> str:
        return self.user.email


class ProductManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # ? product_categories = models.ManyToManyField("ProductCategory", blank=True)
    # ? product_SKUs = models.ManyToManyField("ProductSKU", blank=True)

    product_categories = models.TextField(blank=True)
    product_SKUs = models.TextField(blank=True)

    product_descriptions = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Product Manager")
        verbose_name_plural = _("Product Managers")

    def __str__(self) -> str:
        return self.user.email


class SocialMediaInfluencer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    social_media_profiles = models.TextField(blank=True, null=True)
    follower_count = models.PositiveIntegerField(blank=True, null=True)
    engagement_metrics = models.JSONField(blank=True, null=True)
    content_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Social Media Influencer")
        verbose_name_plural = _("Social Media Influencers")

    def __str__(self) -> str:
        return self.user.email


class SalesRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sales_targets = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Sales Representative")
        verbose_name_plural = _("Sales Representatives")

    def __str__(self) -> str:
        return self.user.email


class LogisticsCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # ? shipping_methods = models.ManyToManyField("ShippingMethod", blank=True)
    shipping_methods = models.TextField(blank=True)
    tracking_information = models.TextField(blank=True, null=True)
    # ? delivery_schedules = models.ManyToManyField("DeliverySchedule", blank=True)
    delivery_schedules = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Logistics Coordinator")
        verbose_name_plural = _("Logistics Coordinators")

    def __str__(self) -> str:
        return self.user.email


class FinancialAnalyst(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    financial_data = models.JSONField(blank=True, null=True)
    # ? reports = models.ManyToManyField("FinancialReport", blank=True)
    reports = models.TextField("FinancialReport", blank=True)
    # ? forecasting_models = models.ManyToManyField("ForecastingModel", blank=True)
    forecasting_models = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Financial Analyst")
        verbose_name_plural = _("Financial Analysts")

    def __str__(self) -> str:
        return self.user.email


class DataAnalyst(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # ? data_sources = models.ManyToManyField('DataSource', blank=True)
    data_sources = models.TextField(blank=True)
    analysis_methodologies = models.TextField(blank=True, null=True)
    # ? reports_generated = models.ManyToManyField('DataReport', blank=True)
    reports_generated = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Data Analyst")
        verbose_name_plural = _("Data Analysts")

    def __str__(self) -> str:
        return self.user.email


class LegalCounsel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # ? legal_documents = models.ManyToManyField("LegalDocument", blank=True)
    legal_documents = models.TextField(blank=True)
    # ? legal_cases = models.ManyToManyField("LegalCase", blank=True)
    legal_cases = models.TextField(blank=True)
    legal_advice = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Legal Counsel")
        verbose_name_plural = _("Legal Counsel")

    def __str__(self) -> str:
        return self.user.email


class InventoryManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    inventory_tracking_data = models.JSONField(blank=True, null=True)
    # ? stock_levels = models.ManyToManyField("StockLevel", blank=True)
    # ? sreorder_points = models.ManyToManyField("ReorderPoint", blank=True)

    class Meta:
        verbose_name = _("Inventory Manager")
        verbose_name_plural = _("Inventory Managers")

    def __str__(self) -> str:
        return self.user.email
