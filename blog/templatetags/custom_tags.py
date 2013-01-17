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
	current_timestamp = datetime.datetime.now()
	post_timestamp = timestamp.replace(tzinfo=None)  # strip off timezone before subtracting else you get this "can't subtract offset-naive and offset-aware datetimes"
	timestamp_difference = current_timestamp - post_timestamp

	time_diff_in_seconds = total_seconds(timestamp_difference)  # total_seconds(timestamp_difference)

	for index, item in enumerate(time_unit_list):
		if time_diff_in_seconds < item.values()[0] and index == 0:
			return "a moment ago"
		elif time_diff_in_seconds < item.values()[0]:
			prev_item = time_unit_list[index - 1]
			diff_in_unit = round(time_diff_in_seconds / prev_item.values()[0])
			return "about %i %s ago" % (diff_in_unit, pluralize(diff_in_unit, prev_item.keys()[0]))
