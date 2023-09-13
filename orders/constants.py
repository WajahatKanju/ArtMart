from django.db.models import TextChoices


class PaymentMethod(TextChoices):
    CARD = "CREDIT/DEBIT CARD", "Credit/Debit Card"
    JAZZCASH = "JAZZCASH", "Jazz Cash"
    EASYPAISA = "EASYPAISA", "Easy Paisa"
    CASH_ON_DELIVERY = "CASH_ON_DELIVERY", "Cash On Delivery"
