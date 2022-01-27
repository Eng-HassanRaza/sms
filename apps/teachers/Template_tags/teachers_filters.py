from django import template
register = template.Library()
@register.filter
def perfomance(value):
