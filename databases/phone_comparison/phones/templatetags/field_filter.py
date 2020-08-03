from django import template

register = template.Library()

@register.filter
def field_filter(value, arg):
    try:
        return value.__getattribute__(arg)
    except AttributeError:
        return '-'