from django import template

register = template.Library()


@register.filter
def get_first_thumbnail(images):
    for image in images:
        if image.is_thumbnail:
            return image
    return None
