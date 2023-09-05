from products.models import Product, ProductImage
from django.core.files import File
from create_essentials import (
    category1,
    # category2,
    # category3,
    # brand1,
    # brand2,
    # brand3,
    # brand4,
    # brand5,
    # brand6,
    # brand7,
    # brand8,
    brand9,
    # attribute1,
    # attribute2,
    # attribute3,
    # attribute4,
    # attribute_value1,
    # attribute_value2,
    # attribute_value3,
    # attribute_value4,
    # attribute_value5,
    # attribute_value6,
    # attribute_value7,
    # attribute_value8,
    # attribute_value9,
    # attribute_value10,
    # attribute_value11,
    # attribute_value12,
    # attribute_value13,
    # attribute_value14,
    # attribute_value15,
)

# wall e
# https://www.youtube.com/watch?v=N63TaxbHT1U

product1 = Product.objects.get_or_create(
    name=" Disney and Pixar WALL-E Robot Toy, Remote Control Hello\
        WALL-E Robot Figure, Gifts for Kids (Amazon Exclusive)",
    category=category1,
    brand=brand9,
    min_purchase_qty=1,
    refunable=True,
    base_price=52.99,
    description="A Nice Product for kids to paly with",
)


product1_image_1 = ProductImage.objects.get_or_create(
    product=product1,
    is_thumbnail=True,
    image=File(open("./images/yellow_rover_with_eyes.jpg", "rb")),
    decription="WALL-E Robot Toy",
)
