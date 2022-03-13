from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from pypass.forms.auth_form import LoginForm
from pypass.models.profile import Profile


class PyPassLoginView(LoginView):
    form_class = LoginForm
    template_name = "pypass/auth_login.html"

    def get_success_url(self):
        self.request.session['profile'] = model_to_dict(Profile.objects.get(user=self.request.user.id))
        return super(PyPassLoginView, self).get_success_url()

    def form_valid(self, form):
        return super(PyPassLoginView, self).form_valid(form)


class PyPassLogoutView(LogoutView):
    next_page = reverse_lazy("pypass:login")
