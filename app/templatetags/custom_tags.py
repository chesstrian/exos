from datetime import date
from django import template

register = template.Library()


@register.filter
def age(birthday):
    if birthday is None:
        return ''

    today = date.today()
    if birthday > today:
        return 0
    else:
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


@register.filter
def eligible(birthday):
    if birthday is None:
        return ''

    if age(birthday) > 13:
        return 'allowed'
    else:
        return 'blocked'


@register.filter
def bizz_fuzz(number):
    result = ''

    if number % 3 == 0:
        result += 'Bizz'
    if number % 5 == 0:
        result += 'Fuzz'

    if result != '':
        return result
    else:
        return number
