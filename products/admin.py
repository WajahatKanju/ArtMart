from django.contrib import admin
from .models import (
    Product,
    ProductImage,
    Category,
    Cart,
    CartItem,
    Review,
)


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
