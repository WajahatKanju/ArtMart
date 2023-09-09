from django.db import models


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SELLER = "SELLER", "Seller/Merchant"


class PaymentPreference(models.TextChoices):
    JAZZ_CASH = "JAZZ_CASH", "Jazz Cash"
    EASYPAISA = "EASY_PAISA", "Easy Paisa"


class BUSINESS_TYPES(models.TextChoices):
    sole_proprietorship = ("sole_proprietorship", "Sole Proprietorship")
    llc = ("llc", "Limited Liability Company (LLC)")
    corporation = ("corporation", "corporation")
