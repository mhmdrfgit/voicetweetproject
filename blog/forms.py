from django import forms
from .models import Post,Tweet,Comment


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title','audio_file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['c_audio_file']

