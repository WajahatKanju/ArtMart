import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]

USER_TYPE_CHOICES = [
    ("customer", "Customer"),
    ("seller", "Seller"),
    ("support", "Support Staff"),
    ("delivery", "Delivery Personnel"),
    ("affiliate", "Affiliate Partners"),
    ("wholesale", "Wholesale Buyers"),
    ("manufacturer", "Manufacturers/Suppliers"),
]


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="custom_user_set",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_user_set",
    )

    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="customer"
    )
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username


class Seller(User):
    shop_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Seller: {self.username}"


class SupportStaff(User):
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Support Staff"


class DeliveryPersonnel(User):
    vehicle_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Delivery Personnel"


class AffiliatePartner(User):
    website = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "Affiliate Partners"


class WholesaleBuyer(User):
    company_name = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Wholesale Buyers"


class Manufacturer(User):
    company_name = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Manufacturers/Suppliers"


class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ("Billing", "Billing Address"),
        ("Shipping", "Shipping Address"),
        ("Mailing", "Mailing Address"),
        ("Residential", "Residential Address"),
        ("Business", "Business Address"),
        ("Work", "Work Address"),
        ("Temporary", "Temporary Address"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "accounts.user", on_delete=models.CASCADE, related_name="addresses"
    )
    address = models.CharField(max_length=255, null=True)
    country_id = models.IntegerField(null=True)
    state_id = models.IntegerField()
    city_id = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    postal_code = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    set_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPE_CHOICES)

    def __str__(self):
        return f"{self.address}, {self.city_id}, {self.country_id}"
