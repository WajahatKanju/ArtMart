from django.db import models
from django.utils.translation import gettext as _
from .constants import PaymentMethod


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, verbose_name=_("Order")
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, verbose_name=_("Product")
    )
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.quantity} x {self.product} in Order #{self.order.pk}"


class OrderStatus(models.Model):
    name = models.CharField(
        _("Status Name"),
        max_length=50,
    )

    class Meta:
        verbose_name = _("Order Status")
        verbose_name_plural = _("Order Statuses")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        "users.Customer", on_delete=models.CASCADE, verbose_name=_("Customer")
    )
    items = models.ManyToManyField(
        "products.Product", through=OrderItem, verbose_name=_("Ordered Items")
    )
    payment_method = models.CharField(
        _("Payment Method"),
        choices=PaymentMethod.choices,  # Replace with your actual PaymentMethod choices
        max_length=50,
    )
    placed_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Placed Date"))
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Order Status"),
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"


class ShippingStatus(models.Model):
    name = models.CharField(
        _("Status Name"),
        max_length=50,
    )

    class Meta:
        verbose_name = _("Shipping Status")
        verbose_name_plural = _("Shipping Statuses")

    def __str__(self):
        return self.name


class Shipping(models.Model):
    order = models.OneToOneField(
        "orders.Order", on_delete=models.CASCADE, verbose_name=_("Order")
    )
    address = models.TextField(_("Shipping Address"))
    tracking_number = models.CharField(
        _("Tracking Number"), max_length=100, unique=True
    )
    status = models.ForeignKey(
        ShippingStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Status"),
    )
    expected_delivery_date = models.DateField(
        _("Expected Delivery Date"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Shipping")
        verbose_name_plural = _("Shipping")

    def __str__(self):
        return f"Shipping for Order #{self.order.pk}"


class Invoice(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, verbose_name=_("Order")
    )
    invoice_number = models.CharField(_("Invoice Number"), max_length=100, unique=True)
    due_date = models.DateField(_("Due Date"), null=True, blank=True)
    payment_status = models.BooleanField(_("Payment Status"), default=False)

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        return f"Invoice for Order #{self.order.pk}"


class Return(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    return_reason = models.TextField(_("Return Reason"))
    return_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Return Date"))

    class Meta:
        verbose_name = _("Return")
        verbose_name_plural = _("Returns")

    def __str__(self):
        return f"Return for Order #{self.order.pk}"


class Cart(models.Model):
    user = models.ForeignKey(
        "users.Customer", on_delete=models.CASCADE, verbose_name=_("Customer")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_("Cart"))
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, verbose_name=_("Product")
    )
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")

    def __str__(self):
        return f"{self.quantity} x {self.product} in Cart #{self.cart.pk}"
