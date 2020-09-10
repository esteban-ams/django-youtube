from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("register/", views.SingUpView.as_view(), name="register"),
    path("login/", views.SingInView.as_view(), name="login"),
    path("logout/", views.SingOutView.as_view(), name="logout"),
]
