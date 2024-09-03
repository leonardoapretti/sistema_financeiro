from django.utils.formats import localize
from django import template

register = template.Library()


@register.filter
def currency_format(number):
    print(localize(number))
    return localize(number)
