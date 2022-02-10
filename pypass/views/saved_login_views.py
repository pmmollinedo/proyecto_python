from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from pypass.forms.saved_logins_form import CreateSavedLoginForm, UpdateSavedLoginForm
from pypass.models.user_logins import UserSavedLogins


class PyPassCreateLoginView(LoginRequiredMixin, CreateView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_create.html'
    model = UserSavedLogins
    form_class = CreateSavedLoginForm
    success_url = reverse_lazy('pypass:list_login')

    def form_valid(self, form):
        logged_user_id = self.request.user.id
        form.instance.app_user_id = logged_user_id
        return super(PyPassCreateLoginView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = "Create"
        context['page_heading_title'] = "Create new Login"
        return context


class PyPassListLoginView(LoginRequiredMixin, ListView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_list.html'
    context_object_name = 'saved_login_list'
    page_heading_title = 'HomeView'

    def get_queryset(self):
        """
        Return the saved logins list filtered by user.
        """
        logged_user_id = self.request.user.id
        return UserSavedLogins.objects.filter(app_user_id=logged_user_id).order_by('id_user_logins')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = "List"
        context['page_heading_title'] = "Saved Logins List"
        return context


class PyPassDetailLoginView(LoginRequiredMixin, DetailView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_detail.html'
    context_object_name = 'saved_login'
    page_heading_title = 'Detail'

    def get_queryset(self):
        """
        Return the logins by user and login_id.
        """
        logged_user_id = self.request.user.id
        login_id = self.kwargs['pk']
        return UserSavedLogins.objects.filter(app_user_id=logged_user_id, id_user_logins=login_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = "Detail"
        context['page_heading_title'] = "Detail"
        return context


class PyPassUpdateLoginView(LoginRequiredMixin, UpdateView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_update.html'
    context_object_name = 'saved_login'
    form_class = UpdateSavedLoginForm
    success_url = reverse_lazy('pypass:list_login')

    def get_queryset(self):
        """
        Return the logins by user and login_id.
        """
        logged_user_id = self.request.user.id
        login_id = self.kwargs['pk']
        return UserSavedLogins.objects.filter(app_user_id=logged_user_id, id_user_logins=login_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = "Update"
        context['page_heading_title'] = "Update"
        return context

    def form_valid(self, form):
        print(form)
        return super(PyPassUpdateLoginView, self).form_valid(form)


class PyPassDeleteLoginView(LoginRequiredMixin, DeleteView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    model = UserSavedLogins
    success_url = reverse_lazy('pypass:list_login')
