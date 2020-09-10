from django import forms
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from .models import *


class NewVideo_Form(CreateView):
    model = Video
    fields = ["title", "description"]


class Coment_Form(CreateView):
    model = Comment
    fields = ["text"]

