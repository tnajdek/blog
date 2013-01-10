import time
import pprint
from calendar import month_name
from blog.models import Post
from django import template

register = template.Library()

@register.inclusion_tag('archive.html')
def archive_dict():
	"""Make a list of months to show archive links."""

	if not Post.objects.count(): return {}

	# set up vars
	year, month = time.localtime()[:2]
	posts = Post.objects.order_by("created")
	first = posts[0]
	fyear = first.created.year
	fmonth = first.created.month
	archive_dict = {}

	# loop over years and months
	for y in range(year, fyear-1, -1):
		start, end = 12, 0
		if y == year: start = month
		if y == fyear: end = fmonth-1

		archive_dict[y] = {}

		for m in range(start, end, -1):
			archive_dict[y][m] = []

	for post in posts:
		archive_dict[post.created.year][post.created.month].append(post)

	return { 'archive_dict' : archive_dict }