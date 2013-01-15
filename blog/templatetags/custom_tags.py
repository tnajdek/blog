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
	return string

# python version < 2.7 don't have deltatime.total_seconds() so I'm using this
def total_seconds(td):
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

@register.filter
def prettify_time(timestamp):

	time_unit_list = [{'minute': MINUTE}, {'hour': HOUR}, {'day': DAY}, {'week': WEEK}, {'month': MONTH}, {'year': YEAR}]
	ret = ''
	current_timestamp = datetime.datetime.now()
	post_timestamp = timestamp.replace(tzinfo=None) # strip off timezone before subtracting else you get this "can't subtract offset-naive and offset-aware datetimes"
	timestamp_difference = current_timestamp - post_timestamp

	timestamp_difference_in_seconds = total_seconds(timestamp_difference)
	for index, item in enumerate(time_unit_list):

		for time_unit in item:
			unit_operand = item[time_unit]

			if timestamp_difference_in_seconds < unit_operand:
				ret = 'a moment ago'

			if index > 0:
				if timestamp_difference_in_seconds < unit_operand:

					time_unit_dict = time_unit_list[index - 1]
					time_unit_key = time_unit_dict.keys()[0]
					time_unit_value = time_unit_dict[time_unit_key]
					
					pretty_value = int(round(timestamp_difference_in_seconds / time_unit_value))
					ret = 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, time_unit_key))
				else:
					ret = 'over a year ago'
	return ret