from django.contrib import admin

from .models import (
    OrderItem,
    OrderStatus,
    Order,
    ShippingStatus,
    Shipping,
    Invoice,
    Return,
    Cart,
    CartItem,
)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    list_filter = ("order", "product")


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "payment_method", "placed_date", "status")
    list_filter = ("user", "placed_date", "status")
    raw_id_fields = ("items",)


@admin.register(ShippingStatus)
class ShippingStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "address",
        "tracking_number",
        "status",
        "expected_delivery_date",
    )
    list_filter = ("order", "status", "expected_delivery_date")


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "invoice_number",
        "due_date",
        "payment_status",
    )
    list_filter = ("order", "due_date", "payment_status")


@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "return_reason", "return_date")
    list_filter = ("order", "return_date")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("user", "created_at")
    date_hierarchy = "created_at"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity")
    list_filter = ("cart", "product")
