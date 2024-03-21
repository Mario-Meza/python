# app/templatetags/mayusculas.py
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='mayusculas')
@stringfilter
def mayusculas(value):
    return value.upper()
