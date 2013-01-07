# from django.forms import ModelForm
from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
	# author = forms.CharField(label='',)
	
	class Meta:
		model = Comment
		fields = ('author', 'body')