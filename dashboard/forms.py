from django import forms
from .models import NeedPost


class CreateNeedPostForm(forms.ModelForm):
    class Meta:
        model = NeedPost
        fields = ["name", "priority"]
