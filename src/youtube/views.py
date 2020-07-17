from django.shortcuts import render
from .forms import NewVideo_Form


# Create your views here.

def new_video(request):

    context = {}

    if request.method == 'POST':
        form = NewVideo_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewVideo_Form()
    context['form'] = form
    return render(request, 'youtube/new_video.html', context)