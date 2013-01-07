import simplejson as json

from django.core import serializers
from django import http
from blog.models import Post, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from datetime import datetime
from django.views.generic.list_detail import object_list

from blog.forms import CommentForm

def index(request):
	posts = Post.objects.all().order_by("-created")
	return object_list(request, template_name = 'index.html',
		queryset = posts, paginate_by = 2)

def view_blog(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments = Comment.objects.filter(post=post)
	context = Context({'title': post.title, 'post': post, 'comments': comments, 'form':CommentForm()})
	return render_to_response("post.html", context, context_instance=RequestContext(request))
	
def tagpage(request, tag):
	posts = Post.objects.filter(tags__name=tag)
	context = {"posts":posts, "tag":tag}
	return render_to_response("tagpage.html", {"posts":posts, "tag":tag}, context_instance=RequestContext(request))

def add_comment(request, post_id):
	if request.method == "POST":
		comment_object = {}
		# for security reasons, grab id like so: request.POST.get('post_id||pk||slug')
		form = CommentForm(request.POST)
		if request.is_ajax():
			if form.is_valid():
				post = Post.objects.all().get(pk=post_id)
				comment = form.save(commit=False)
				comment.post = post
				comment.save()
				# or just use data from "form", instead of going back to pull data from model
				# comment_object = serializers.serialize('json', [Comment.objects.get(pk=comment.id)], ensure_ascii=False)
				comment_object['author'] = comment.author
				comment_object['body'] = comment.body
				comment_object['posted_on'] = comment.posted_on.strftime('%b. %d, %Y, %I:%M %p') 
				resp = {
					'error': False,
					'data':  comment_object, # comment_object[1:-1]
					'id': request.POST.get('pk')
				}
			else:
				resp = {
					'error': True,
					# '': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])
					'errors': dict(form.errors.items())
				}
			return http.HttpResponse(json.dumps(resp), mimetype='application/json')
		if form.is_valid():
			post = Post.objects.all().get(pk=post_id)
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return http.HttpResponseRedirect(post.get_absolute_url())
	else:
		form = CommentForm()
	# context = Context({'form': form})
	return render_to_response('comments/form.html', {'form': form}, RequestContext(request))
