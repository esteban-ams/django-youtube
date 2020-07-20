from django.shortcuts import render
from .forms import NewVideo_Form
from .models import *

# Create your views here.

def index(request):

    context = {}
    videos = Video.objects.all()
    context['videos'] = videos  
    return render(request, 'youtube/index.html', context)

def new_video(request):

    context = {}

    if request.method == 'POST':
        form = NewVideo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NewVideo_Form()
    context['form'] = form
    return render(request, 'youtube/new_video.html', context)