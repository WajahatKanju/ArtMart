from products.models import (
    Brand,
    Category,
    VideoProvider,
    Attribute,
    AttributeValue,
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
