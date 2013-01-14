#!/usr/bin/python
import os, sys, time, datetime, math
import cProfile

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7
YEAR = DAY * 365
MONTH = YEAR / 12

some_day = datetime.datetime(2012, 7, 1, 16, 55, 45)

now = datetime.datetime.now()
time_diff = now - some_day

alpha_list = [{'minute': MINUTE}, {'hour': HOUR}, {'day': DAY}, {'week': WEEK}, {'month': MONTH}, {'year': YEAR}]

time_diff_in_seconds = time_diff.total_seconds()

def pluralize(value, string):
	if value > 1:
		return string + 's'
	return string

# un-DRY version, better readability but with IF-ELSE block we could do without 
def prettify_time(time_diff_in_seconds):

	if time_diff_in_seconds < MINUTE:
		return 'just now'
	elif time_diff_in_seconds < HOUR:
		pretty_value = int(round(time_diff_in_seconds / MINUTE))
		return 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'minute')) 
	elif time_diff_in_seconds < DAY:
		pretty_value = int(round(time_diff_in_seconds / HOUR))
		return 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'hour'))
	elif time_diff_in_seconds < WEEK:
		pretty_value = int(round(time_diff_in_seconds / DAY))
		return 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'day'))
	elif time_diff_in_seconds < MONTH:
		pretty_value = int(round(time_diff_in_seconds / WEEK))
		return 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'week'))
	elif time_diff_in_seconds < YEAR:
		pretty_value = int(round(time_diff_in_seconds / MONTH))
		return 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, 'month'))
	else:
		return 'over a year ago'

print prettify_time(time_diff_in_seconds)

# Profile for optimisation. 6 function calls
cProfile.run('prettify_time(time_diff_in_seconds)')


# DRY version without the craaayy IF-ELSE block but a tad more complex and less readable
def prettify_time_dry(time_diff_in_seconds):
	ret = ''
	for index, item in enumerate(alpha_list):

		for time_unit in item:
			unit_operand = item[time_unit]

			if time_diff_in_seconds < unit_operand:
				ret = 'a moment ago'
				
			if index > 0:
				if time_diff_in_seconds < unit_operand:

					unit_dict = alpha_list[index - 1]
					unit_key = unit_dict.keys()[0]
					unit_value = unit_dict[unit_key]
					
					pretty_value = int(round(time_diff_in_seconds / unit_value))
					ret = 'about {0} {1} ago'.format(pretty_value, pluralize(pretty_value, unit_key))
				else:
					ret = 'over a year ago'
	return ret

print prettify_time_dry(time_diff_in_seconds)

# Profile for optimisation 7 function calls (+ {method 'keys' of 'dict' objects} )
cProfile.run('prettify_time_dry(time_diff_in_seconds)')
