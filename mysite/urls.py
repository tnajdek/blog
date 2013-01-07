from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from django.contrib import admin, comments
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^comments/', include('django.contrib.comments.urls')),
)
