from django import forms
from django.contrib.auth import authenticate
from .models import *

class NewVideo_Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'file']

class Coment_Form(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = '__all__'
    