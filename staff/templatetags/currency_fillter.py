from django import template

register = template.Library()

@register.filter(name='currency_format')
def currency_format(value):
    try:
        value = int(value)
        return "{:,.0f} VND".format(value)
    except (TypeError, ValueError):
        return value