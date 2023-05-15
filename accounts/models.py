import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    USER_TYPE_CHOICES = [
        ("customer", "Customer"),
        ("seller", "Seller"),
        ("admin", "Admin"),
        ("support", "Support Staff"),
        ("delivery", "Delivery Personnel"),
        ("affiliate", "Affiliate Partners"),
        ("wholesale", "Wholesale Buyers"),
        ("manufacturer", "Manufacturers/Suppliers"),
    ]

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

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
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
