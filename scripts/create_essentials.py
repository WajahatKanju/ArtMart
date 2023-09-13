from django.core.files import File
from django.db import IntegrityError
from products.models import (
    Product,
    ProductImage,
    ProductVideo,
    ProductVariation,
    ProductPrice,
)
from users.models import User, Seller
from users.constants import PaymentPreference, Role, BUSINESS_TYPES
from .data import products_data


try:
    user, _ = User.objects.get_or_create(
        first_name="Script",
        last_name="Seller",
        email="scripts@seller.com",
        is_staff=True,
        is_active=False,
        bank_name="National Bank Of Pakistan",
        bank_account_number="5157 4258 5408 8415",
        payment_preferences=PaymentPreference.JAZZ_CASH,
        role=Seller,
        phone="03454575251",
    )


except IntegrityError:
    user = User.objects.get(email="scripts@seller.com")

seller, _ = Seller.objects.get_or_create(
    user=user,
    company_name="Fictional Interactive",
    business_registration_number=" 5157 4258 5408 8415",
    tax_identification_number="5157 4258 5408 8415",
    business_type=BUSINESS_TYPES.llc,
)

# Loop through the product data and create products
for product_data in products_data:
    product_images_data = product_data.pop("images")
    variation_data = product_data.pop("variation")
    video_data = product_data.pop("video_data")

    product_data["seller"] = seller
    product, created = Product.objects.get_or_create(**product_data)

    # Create product images
    product_images = []
    previous_images = ProductImage.objects.filter(product=product)
    previous_images.delete()
    for image_data in product_images_data:
        try:
            product_image, created = ProductImage.objects.get_or_create(
                product=product,
                is_thumbnail=image_data["is_thumbnail"],
                image=File(open(image_data["image_path"], "rb")),
                description=image_data["description"],
            )
            product_images.append(product_image)
        except FileNotFoundError as e:
            # Handle the FileNotFoundError, e.g., log it or raise a validation error
            # You can also choose to skip this image and continue processing others
            print(f"File not found: {e}")

    # Create product video
    product_video, created = ProductVideo.objects.get_or_create(
        product=product,
        video_provider=video_data["video_provider"],
        video_link=video_data["video_link"],
    )

    # Create product variation
    variation_data["product"] = product
    attributes = variation_data.pop("attributes")
    product_variation, created = ProductVariation.objects.get_or_create(
        **variation_data
    )
    product_variation.attributes.add(*attributes)

    # Create product price
    product_price, created = ProductPrice.objects.get_or_create(
        product_variation=product_variation,
        unit_price=product_data["base_price"],
    )
