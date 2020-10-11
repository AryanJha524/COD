from django import forms
from .models import HaveToilet


# class CreateCommentForm(forms.ModelForm):
#   class Meta:
#       model = Comment
#      fields = ["name", "text"]


class CreateHaveToiletForm(forms.ModelForm):
    class Meta:
        model = HaveToilet
        fields = ['image', 'description']
