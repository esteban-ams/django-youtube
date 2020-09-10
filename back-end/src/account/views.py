from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    login_required,
    logout_then_login,
)
from django.utils.http import is_safe_url
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    login,
    logout,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

# Create your views here.
from .forms import UserRegister, LoginForm


class SingUpView(FormView):
    template_name = "account/register.html"
    form_class = UserRegister
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        return super().form_valid(form)


class SingInView(LoginView):
    template_name = "account/login.html"
    form_class = LoginForm


class SingOutView(LogoutView):
    pass
