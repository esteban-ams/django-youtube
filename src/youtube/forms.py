from django import forms
from django.contrib.auth import authenticate
from .models import *

class NewVideo_Form(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'