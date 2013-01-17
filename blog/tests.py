"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import Template, Context
from models import Post
from datetime import datetime, timedelta


# helper method
def prettify_date_using_templatag(post):
	return Template(
		'{% load custom_tags %}'
		'{{ post.created|prettify_date }}'
	).render(Context({"post": post}))


class BlogTest(TestCase):
	fixtures = ['sample_posts']
	def setUp(self):
		# Update posts created date
		self.recentPost = Post.objects.all()[0]
		self.recentPost.created = datetime.now() - timedelta(seconds=20)

		self.freshPost = Post.objects.all()[1]
		self.freshPost.created = datetime.now() - timedelta(hours=5)

		self.oldPost = Post.objects.all()[2]
		self.oldPost.created = datetime.now() - timedelta(days=70)

	def test_prettify(self):
		"""
		Test if prettify_date template tag is working fine
		"""

		self.assertEqual(prettify_date_using_templatag(self.recentPost), "a moment ago")
		self.assertEqual(prettify_date_using_templatag(self.freshPost), "5 hours ago")
		self.assertEqual(prettify_date_using_templatag(self.oldPost), "2 months ago")

