from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .constants import Role, PaymentPreference, BUSINESS_TYPES


class User(AbstractBaseUser, PermissionsMixin):
    base_role = Role.ADMIN

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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)


class Seller(User):
    base_role = Role.SELLER

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

    def number_of_products(self):
        return self.products.count()
