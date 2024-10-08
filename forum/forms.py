from django import forms
from .models import Posts, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "description"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
