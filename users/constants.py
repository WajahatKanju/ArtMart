from django.db import models


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SELLER = "SELLER", "Seller/Merchant"
    CUSTOMER = "CUSTOMER", "CUSTOMER/Shopper"
    AFFILIATE_MARKETER = "AFFILIATE_MARKETER", "Affiliate Marketer"
    CUSTOMER_SERVICE_REPRESENTATIVE = (
        "CUSTOMER_SERVICE_REPRESENTATIVE",
        "Customer Service Representative",
    )
    DELIVERY_DRIVER = "DELIVERY_DRIVER", "Delivery Driver"
    MARKETING_MANAGER = "MARKETING_MANAGER", "Marketing Manager"
    PRODUCT_MANAGER = "PRODUCT_MANAGER", "Product Manager"
    SOCIAL_MEDIA_INFLUENCER = "SOCIAL_MEDIA_INFLUENCER", "Social Media Influencer"
    SALES_REPRESENTATIVE = "SALES_REPRESENTATIVE", "Sales Representative"
    LOGISTICS_COORDINATOR = "LOGISTICS_COORDINATOR", "Logistics Coordinator"
    LEGAL_COUNSEL = "LEGAL_COUNSEL", "Legal Counsel"
    FINANCIAL_ANALYST = "FINANCIAL_ANALYST", "Financial Analyst"
    DATA_ANALYST = "DATA_ANALYST", "Data Analyst"
    INVENTORY_MANAGER = "INVENTORY_MANAGER", "Inventory Manager"


class BUSINESS_TYPES(models.TextChoices):
    sole_proprietorship = ("sole_proprietorship", "Sole Proprietorship")
    llc = ("llc", "Limited Liability Company (LLC)")
    corporation = ("corporation", "corporation")
