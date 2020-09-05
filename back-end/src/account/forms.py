from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegister(UserCreationForm):
    telefono = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'telefono', 'password1', 'password2']
