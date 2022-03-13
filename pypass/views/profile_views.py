from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from pypass.forms.profile_form import ProfileForm, UserForm
from pypass.models.profile import Profile


class PyPassProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/profile_detail.html'
    context_object_name = 'saved_login'
    model = Profile
    form_class = ProfileForm
    second_form_class = UserForm
    success_url = reverse_lazy('pypass:profile')

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("pypass:profile", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super(PyPassProfileUpdateView, self).get_context_data()
        context["web_title"] = "Profile"
        context['page_heading_title'] = "Profile"

        if 'user_form' not in context:
            if 'user_form' in kwargs:
                # if in kwargs means user_form invalid (username in use)
                context['user_form'] = kwargs["user_form"]
                self.request.user = User.objects.get(id=self.request.user.id)
            else:
                context['user_form'] = UserForm(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile_form = self.form_class(request.POST)
        user_form = self.second_form_class(request.POST, instance=self.request.user)

        if profile_form.is_valid() and user_form.is_valid():
            userdata = user_form.save(commit=False)
            pwd = user_form["password"].value()
            conf_pwd = user_form["confirm_password"].value()
            if pwd and conf_pwd and (pwd == conf_pwd):
                userdata.set_password(pwd)
            userdata.save()
            messages.success(self.request, 'Settings saved successfully')
            post_return = super(PyPassProfileUpdateView, self).post(request, *args, **kwargs)
        else:
            post_return = self.render_to_response(self.get_context_data(form=profile_form, user_form=user_form))

        self.request.session['profile'] = model_to_dict(Profile.objects.get(user=self.request.user.id))
        return post_return

    def form_valid(self, form):
        return super(PyPassProfileUpdateView, self).form_valid(form)


class PyPassProfileDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    model = User
    success_url = reverse_lazy('pypass:login')


