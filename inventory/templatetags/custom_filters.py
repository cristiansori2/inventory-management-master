from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(value, arg):
    """Gets an item from a list using its index."""
    try:
        return value[arg]
    except IndexError:
        return ''