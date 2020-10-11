from django import forms
from .models import NeedPost, Comment, HaveToilet


class CreateNeedPostForm(forms.ModelForm):
    class Meta:
        model = NeedPost
        fields = ["name", "priority"]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text"]


class CreateHaveToiletForm(forms.ModelForm):
    class Meta:
        model = HaveToilet
        fields = ['image', 'description']
