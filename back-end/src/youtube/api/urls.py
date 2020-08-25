from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from youtube.api import views

urlpatterns = [
    path('video_detail/<int:pk>/', views.VideoDetail.as_view()),
    path('video_list/', views.VideoList.as_view()),
    path('comment/<int:pk>/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
