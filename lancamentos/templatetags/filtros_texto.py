from django import template

register = template.Library()


# @register.filter(name='opcional')
@register.filter
def boolean_format(boolean):
    if boolean == True:
        return 'Sim'
    return 'Não'

# register.filter('boolean_format', boolean_format)

# exemplo data
# @register.filter(expects_localtime=True)
# def businesshours(value):
#     try:
#         return 9 <= value.hour < 17
#     except AttributeError:
#         return ""
