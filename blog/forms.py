from .models import Comment
from .models import Post
from django import forms


#-------------------------------------------------------------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#-------------------------------------------------------------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
