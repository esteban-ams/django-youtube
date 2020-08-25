from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registerForm(request):
    
    form = UserCreationForm()
    context['form'] = form
    return render(request, 'account/register.html', context)

