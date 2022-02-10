from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from pypass.forms.auth_form import LoginForm


class PyPassLoginView(LoginView):
    form_class = LoginForm
    template_name = "pypass/auth_login.html"


class PyPassLogoutView(LogoutView):
    next_page = reverse_lazy("pypass:login")
