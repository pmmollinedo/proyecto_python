from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from pypass.forms.auth_form import LoginForm, RegisterForm
from pypass.models.profile import Profile


class PyPassLoginView(LoginView):
    form_class = LoginForm
    template_name = "pypass/auth_login.html"

    def get_success_url(self):
        self.request.session['profile'] = model_to_dict(Profile.objects.get(user=self.request.user.id))
        return super(PyPassLoginView, self).get_success_url()

    def get_context_data(self, **kwargs):
        context = super(PyPassLoginView, self).get_context_data(**kwargs)
        context["web_title"] = "Login"
        return context


class PyPassLogoutView(LogoutView):
    next_page = reverse_lazy("pypass:login")


class PyPassRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "pypass/auth_register.html"
    success_url = reverse_lazy('pypass:login')

    def get_context_data(self, **kwargs):
        context = super(PyPassRegisterView, self).get_context_data(**kwargs)
        context["web_title"] = "Register"
        return context
