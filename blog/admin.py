from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ["title"]

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/js/tiny_mce.js',
		]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)