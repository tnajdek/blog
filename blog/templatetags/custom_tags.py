import calendar
import datetime
import sys

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7
YEAR = DAY * 365
MONTH = YEAR / 12

@register.filter
@stringfilter
def trim(value):
	return value.strip()

@register.filter
def month_name(month_number):
	return calendar.month_name[month_number]

def pluralize(value, string):
	if value > 1:
		return string + 's'
	else:
		return string

# python version < 2.7 don't have deltatime.total_seconds() so I'm using this
def total_seconds(td):
	return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

@register.filter
def prettify_date(timestamp):

	time_unit_list = [{'minute': MINUTE}, {'hour': HOUR}, {'day': DAY}, {'week': WEEK}, {'month': MONTH}, {'year': YEAR}]
	ret = ''
	current_timestamp = datetime.datetime.now()
	post_timestamp = timestamp.replace(tzinfo=None) # strip off timezone before subtracting else you get this "can't subtract offset-naive and offset-aware datetimes"
	timestamp_difference = current_timestamp - post_timestamp

	timestamp_difference_in_seconds = total_seconds(timestamp_difference) #total_seconds(timestamp_difference)
	
	if timestamp_difference_in_seconds < MINUTE:
		return 'a moment ago'
	elif timestamp_difference_in_seconds < HOUR:
		pretty_value = int(round(timestamp_difference_in_seconds / MINUTE))
		return '{0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'minute')) 
	elif timestamp_difference_in_seconds < DAY:
		pretty_value = int(round(timestamp_difference_in_seconds / HOUR))
		return '{0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'hour'))
	elif timestamp_difference_in_seconds < WEEK:
		pretty_value = int(round(timestamp_difference_in_seconds / DAY))
		return '{0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'day'))
	elif timestamp_difference_in_seconds < MONTH:
		pretty_value = int(round(timestamp_difference_in_seconds / WEEK))
		return '{0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'week'))
	elif timestamp_difference_in_seconds < YEAR:
		pretty_value = int(round(timestamp_difference_in_seconds / MONTH))
		return '{0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'month'))
	else:
		return 'over a year ago'
