import locale

from django import template

register = template.Library()


@register.filter
def currency_format(number):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(number, grouping=True, symbol=None)

    return f'R$ {valor}'
