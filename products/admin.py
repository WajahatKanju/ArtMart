from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
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
)
from django.utils.html import format_html, mark_safe


class ProductPriceInline(NestedStackedInline):
    model = ProductPrice
    max_num = 1
    min_num = 1
    extra = 1


class ProductVariationInline(NestedTabularInline):
    model = ProductVariation
    min_num = 1
    extra = 0

    inlines = [ProductPriceInline]


class ProductVideoInline(NestedTabularInline):
    model = ProductVideo
    min_num = 1
    extra = 0


class ProductImageInline(NestedTabularInline):
    model = ProductImage
    min_num = 1
    extra = 0
    list_display = ("Image", "Description" "display_image")
    readonly_fields = ["display_image"]

    def display_image(self, obj):
        # Display the image as an inline thumbnail
        return format_html('<img src="{}" width="100" />', obj.image.url)

    display_image.short_description = "Image Preview"


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "prices",
        "product_image",
        "product_video",
        "created_at",
        "updated_at",
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
            product_videos = obj.videos.all()
            if product_videos:
                video_links = [
                    format_html(
                        '<span>{}:&nbsp;<a href="{}"\
                            target="_blank">Video Link</a></span>',
                        product_video.video_provider,
                        product_video.video_link,
                    )
                    for product_video in product_videos
                    if product_video.video_link
                ]
                return mark_safe("<br>".join(video_links))
        except ProductVideo.DoesNotExist:
            pass

        return "No Video Link"

    def prices(self, obj):
        variations = obj.variations.all()
        price_info = ""
        for variation in variations:
            prices = variation.product_variation.all()
            for price in prices:
                attributes = price.product_variation.attributes.all()
                attribute_names = [attr.value for attr in attributes]
                print(attribute_names)
                price_info += f"Type: {attribute_names}<br>"
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
    model = Attribute.values.through  # Use the related name through the ManyToManyField
    extra = 1


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    inlines = [AttributeValueInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Automatically create AttributeValue instances when saving Attribute
        values = request.POST.getlist("values")
        for value_id in values:
            obj.values.add(value_id)
