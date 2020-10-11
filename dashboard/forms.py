from django import forms
from .models import NeedPost, Comment


class CreateNeedPostForm(forms.ModelForm):
    class Meta:
        model = NeedPost
        fields = ["name", "priority"]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text"]
