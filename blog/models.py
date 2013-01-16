from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	slug = models.SlugField(max_length=255, unique=True)
	tags = TaggableManager()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s.html" % (self.slug)

	# self.created.year, self.created.month,

class Comment(models.Model):
	author = models.CharField(max_length=25)
	body = models.TextField()
	email = models.EmailField(blank=True)
	posted_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)