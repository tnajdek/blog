import calendar
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def trim(value):
	return value.strip()

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]
