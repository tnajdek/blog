# from django.forms import ModelForm
from django.forms import ModelForm, Textarea, TextInput
from blog.models import Comment

class CommentForm(ModelForm):
	# author = forms.CharField(label='',)
	
	class Meta:
		model = Comment
		fields = ('body','author','email')
		widgets = {
			'email': TextInput({'placeholder': 'Email'}),
			'author': TextInput({'placeholder': 'Name', 'class':'input-medium'}),
            'body': Textarea(attrs={'rows': 4, 'placeholder': 'Add a comment . . .', 'class': 'custom'})
        }