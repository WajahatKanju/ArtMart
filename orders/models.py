from django.db import models
from django.utils.translation import gettext_lazy as _
from .constants import PaymentMethod


class Order(models.Model):
    user = models.ForeignKey("users.Customer", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    payment_method = models.CharField(
        _("Payment Method"), choices=PaymentMethod.choices, max_length=50
    )
    placed_date = models.DateTimeField(auto_created=True)
