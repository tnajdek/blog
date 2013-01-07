from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('blog.views',

	# url(r'^$', ListView.as_view(
	# 			queryset = Post.objects.all().order_by("-created"),
	# 			template_name = "index.html",
	# 	)),

	url(r'^$', 'index'),

	# url(r'^(?P<pk>\d+)/$', DetailView.as_view(
	# 			model=Post,
	# 			template_name="post.html"
	# 	)),

	url(r'^(?P<slug>[\w-]+).html$', 'view_blog'),
    url(r'^comment/add/(\d+)/$', 'add_comment'),

	# url(r'^(?P<slug>[\w-]+).html$', DetailView.as_view(
	# 			model=Post,
	# 			template_name="post.html"
	# 	)),
	# url(r'^archives/$', DetailView.as_view(
	# 			model = Post,
	# 			template_name = "archives.html"
	# 	)),
	url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
)