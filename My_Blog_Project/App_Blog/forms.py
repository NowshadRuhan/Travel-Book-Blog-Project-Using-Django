from django import forms
from App_Blog.models import Blog, Comment, Likes

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="",widget=forms.TextInput(
    attrs={'style':'height:60px;', 'placeholder':'Enter Your Comment'}))
    class Meta:
        model = Comment
        fields = ['comment']
