from django import template

register = template.Library()


@register.filter(name='color')
def get_color(value):
    try:
        value = float(value)
    except ValueError:
        return ''
    if value < 0:
        return '#0f7003'
    elif 1 <= value < 2:
        return '#fbc8c9'
    elif 2 <= value < 5:
        return '#f6767a'
    elif value >= 5:
        return '#fb0008'
    else:
        return ''
