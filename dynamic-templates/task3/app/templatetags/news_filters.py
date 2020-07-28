from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def format_date(value):
    date = datetime.fromtimestamp(value)
    delta = datetime.now() - date
    if delta <= timedelta(minutes=10):
        return 'только что'
    elif delta < timedelta(hours=1):
        minutes = round(delta.seconds / 60)
        return f'{minutes} минут назад'
    elif delta < timedelta(hours=24):
        hours = round(delta.seconds / (60 * 60))
        return f'{hours} часов назад'
    else:
        return date.strftime('y-M-d')


# необходимо добавить фильтр для поля `score`

@register.filter
def score(value, arg=None):
    if not value:
        return arg
    if value <= -5:
        return 'все плохо'
    elif value <= 5:
        return 'нейтрально'
    else:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    elif value > 50:
        return '50+'


@register.filter
def format_selftext(value, count=3):
    print(value)
    words = value.split(' ')
    if len(words) > (count * 2) + 1:
        return ' '.join([*words[:5], '...', *words[-5:]])
    return value
