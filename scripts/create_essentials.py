from django.core.files import File
from products.models import (
    Brand,
    Category,
    VideoProvider,
    Attribute,
    AttributeValue,
    Product,
    ProductImage,
    ProductVideo,
    ProductVariation,
    ProductPrice,
)


def get_or_create_category(name):
    category, created = Category.objects.get_or_create(name=name)
    return category


def get_or_create_brand(name):
    brand, created = Brand.objects.get_or_create(name=name)
    return brand


def get_or_create_video_provider(name):
    video_provider, created = VideoProvider.objects.get_or_create(name=name)
    return video_provider


def get_or_create_attribute(name):
    attribute, created = Attribute.objects.get_or_create(name=name)
    return attribute


def get_or_create_attribute_value(attribute, value):
    attribute_value, created = AttributeValue.objects.get_or_create(
        attribute=attribute, value=value
    )
    return attribute_value


# Create categories
category1 = get_or_create_category("Electronics")
category2 = get_or_create_category("Cosmetics")
category3 = get_or_create_category("Foods")

# Create brands
brands_data = [
    "Skull Candy",
    "Robotiatoys",
    "P&G",
    "Granier",
    "Unilever",
    "Nestle",
    "Shan",
    "National Foods",
    "Disney",
]

brands = [get_or_create_brand(name) for name in brands_data]

# Create video providers
video_provider1 = get_or_create_video_provider("Youtube")
video_provider2 = get_or_create_video_provider("Dailymotion")

# Create Some Attributes
attributes_data = ["color", "size", "type", "material"]

attributes = [get_or_create_attribute(name) for name in attributes_data]

# Create Some Attribute Values
attribute_values_data = [
    ("color", ["red", "green", "yellow", "pink", "blue"]),
    ("size", ["Small", "Medium", "Large", "Extra Large"]),
    ("type", ["Dairy", "meat", "Floral"]),
    ("material", ["Steel", "plastic", "Titanum"]),
]

attribute_values = []

for attribute_name, values in attribute_values_data:
    attribute = [attr for attr in attributes if attr.name == attribute_name][0]
    attribute_values.extend(
        [get_or_create_attribute_value(attribute, value) for value in values]
    )

product_data = {
    "name": "Disney and Pixar WALL-E Robot Toy, Remote Control Hello WALL-E Robot\
        Figure, Gifts for Kids (Amazon Exclusive)",
    "category": category1,
    "brand": brands[-1],
    "min_purchase_qty": 1,
    "refundable": True,
    "base_price": 52.99,
    "description": "A Nice Product for kids to play with",
}

product1, created = Product.objects.get_or_create(**product_data)

product_images_data = [
    {
        "product": product1,
        "is_thumbnail": True,
        "image_path": "./scripts/images/yellow_rover_with_eyes.jpg",
        "description": "WALL-E",
    },
    {
        "product": product1,
        "is_thumbnail": False,
        "image_path": "./scripts/images/sizes yellow rovers.jpg",
        "description": "WALL-E",
    },
    {
        "product": product1,
        "is_thumbnail": False,
        "image_path": "./scripts/images/yello_rover_with_kids.jpg",
        "description": "bot Toy",
    },
]

product_images = []

for image_data in product_images_data:
    product_image, created = ProductImage.objects.get_or_create(
        product=image_data["product"],
        is_thumbnail=image_data["is_thumbnail"],
        image=File(open(image_data["image_path"], "rb")),
        description=image_data["description"],
    )
    product_images.append(product_image)

product1_video_1, created = ProductVideo.objects.get_or_create(
    product=product1,
    video_provider=video_provider1,
    video_link="https://www.youtube.com/watch?v=7oVSaUWeKt0",
)

product_variation_data = {
    "product": product1,
    "stock_quantity": 45,
}

product1_variation1, created = ProductVariation.objects.get_or_create(
    **product_variation_data
)


product1_variation1.attributes.add(attribute_values[2], attribute_values[6])

product1_variation1_price, created = ProductPrice.objects.get_or_create(
    product_variation=product1_variation1,
    unit_price=product_data["base_price"],
)
