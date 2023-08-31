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
    Attribute,
    AttributeValue,
)
from django.utils.html import format_html


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    min_num = 1
    extra = 0


class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    min_num = 1
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    min_num = 1
    extra = 0

    readonly_fields = ["display_image"]

    def display_image(self, obj):
        # Display the image as an inline thumbnail
        return format_html('<img src="{}" width="100" />', obj.image.url)

    display_image.short_description = "Image Preview"


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

    inlines = [
        # ProductPriceInline,
        ProductVariationInline,
        ProductVideoInline,
        ProductImageInline,
    ]


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


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    min_num = 1
    extra = 0


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )
    list_filter = ("name",)
    search_fields = ("name",)
    inlines = [AttributeValueInline]
