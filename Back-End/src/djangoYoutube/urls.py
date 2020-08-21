"""djangoYoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from youtube.views import *
from account.views import *
from django.conf import settings

urlpatterns = [

# Account urls
    path('registration/', registration_view , name='registration'),
    path('login/', login_view , name='login'),
    path('logout/', logout_view , name='logout'),
    path('account/', account_view , name='account'),
    
    path('admin/', admin.site.urls),

#platform urls for daily use
    path('', index, name='index'),
    path('new_video/', new_video, name='newvideo'),
    path('video/<pk>/', video,  name='video'),

# REST APIs
    path('', include('youtube.api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)