from django import forms
from . import models
from.models import Comment

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb',]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email','body')
