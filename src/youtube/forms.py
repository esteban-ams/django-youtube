from django import forms
from django.contrib.auth import authenticate
from .models import *

class NewVideo_Form(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    file = forms.FileField(required=True)

class Coment_Form(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = '__all__'
    