from django.contrib import admin
from .models import (
    Brand,
    Category,
    Product,
    VideoProvider,
    ProductImage,
    ProductVideo,
    ProductVariation,
    ProductPrice,
)
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "prices",
        "created_at",
        "updated_at",
        "product_image",
        "product_video",
    )
    list_filter = ("category", "brand")

    def product_image(self, obj):
        try:
            product_image = obj.images.get(is_thumbnail=True)
            if product_image.image.url:
                return format_html(
                    '<img src="{}" style="max-height: 100px; margin: 5px;" />',
                    product_image.image.url,
                )
        except ProductImage.DoesNotExist:
            pass

        return "None"

    def product_video(self, obj):
        try:
            product_video = obj.videos.get()
            if product_video.video_link:
                return format_html(
                    '<span>{}:&nbsp;<a href="{}" target="_blank">Video Link</a></span>',
                    product_video.video_provider,
                    product_video.video_link,
                )
        except ProductVideo.DoesNotExist:
            pass

        return "No Video Link"

    def prices(self, obj):
        variations = obj.variations.all()
        price_info = ""
        for variation in variations:
            prices = variation.productprice_set.all()
            for price in prices:
                price_info += f"Attributes: {', '.join(attr.name for attr in price.attributes.all())}<br>"
                price_info += f"Unit Price: {price.unit_price}<br>"
                price_info += f"Discount: {price.discount}%<br>"
                price_info += f"Discount Start Date: {price.discount_start_date}<br>"
                price_info += f"Discount End Date: {price.discount_end_date}<br>"
                price_info += "<br>"

        if price_info:
            return format_html(price_info)
        else:
            return "Not Available"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )


@admin.register(VideoProvider)
class VideoProviderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "is_thumbnail", "image_thumbnail", "description")
    list_filter = ("product", "is_thumbnail")

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 100px; max-height: 100px;" />',
                obj.image.url,
            )
        else:
            return "No Image"

    image_thumbnail.short_description = "Thumbnail"


@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ("video_provider", "video_link", "created_at", "updated_at")


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ("product", "attributes", "attribute_value", "created_at")


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_variation",
        "get_attributes",
        "unit_price",
        "discount_start_date",
        "discount_end_date",
        "discount",
        "created_at",
        "updated_at",
    )

    def get_attributes(self, obj):
        return ", ".join([attr.name for attr in obj.attributes.all()])

    get_attributes.short_description = "Attributes"
