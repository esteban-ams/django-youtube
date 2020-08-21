from django.urls import path
from youtube.api import views

urlpatterns = [
    path('video_detail/<int:pk>/', views.video_detail),
    path('video_list/', views.video_list),
]
