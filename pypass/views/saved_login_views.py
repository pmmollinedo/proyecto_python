from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from pypass.forms.saved_logins_form import SavedLoginForm
from pypass.models.user_logins import UserSavedLogin, BrandIcon
from pypass.utils import password_util as pwd_util


class PyPassCreateLoginView(LoginRequiredMixin, CreateView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_create.html'
    model = UserSavedLogin
    form_class = SavedLoginForm
    success_url = reverse_lazy('pypass:list_login')

    def get_form(self, *args, **kwargs):
        form = super(PyPassCreateLoginView, self).get_form(*args, **kwargs)
        # Overwritten field in form to show only enabled icons
        form.fields['brand_icon'].queryset = BrandIcon.objects.filter(is_activated=True)
        return form

    def form_valid(self, form):
        logged_user_id = self.request.user.id
        form.instance.app_user_id = logged_user_id
        plain_password = form.instance.password
        if plain_password:
            token_password = pwd_util.generate_password_token(plain_password)
            form.instance.password = token_password
        return super(PyPassCreateLoginView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["web_title"] = "Create"
        context['page_heading_title'] = "Create new Login"
        context['brand_icons_list'] = BrandIcon.objects.filter(is_activated=True)
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
        return UserSavedLogin.objects.filter(app_user_id=logged_user_id).order_by('id_user_logins')

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
        return UserSavedLogin.objects.filter(app_user_id=logged_user_id, id_user_logins=login_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        logged_user_id = self.request.user.id
        login_id = self.kwargs['pk']
        saved_login = UserSavedLogin.objects.get(app_user_id=logged_user_id, id_user_logins=login_id)
        password_token = saved_login.password
        if password_token:
            saved_login.password = pwd_util.show_password(password_token)

        context['saved_login'] = saved_login
        context["web_title"] = "Detail"
        context['page_heading_title'] = "Detail"
        return context


def get_form_with_decrypted_password(form):
    """
    Method that overrides the form to decrypt the password item
    :return: ModelForm object with decrypted password value
    """
    sitename = form["sitename"].value()
    brand_icon = form["brand_icon"].value()
    username = form["username"].value()
    email = form["email"].value()
    password = pwd_util.show_password(form["password"].value())
    notes = form["notes"].value()
    is_fav = form["is_fav"].value()
    initial_items = {'sitename': sitename, 'brand_icon': brand_icon, 'username': username, 'email': email,
                     'password': password, 'notes': notes, 'is_fav': is_fav}
    return SavedLoginForm(initial=initial_items)


class PyPassUpdateLoginView(LoginRequiredMixin, UpdateView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    template_name = 'pypass/saved_logins_update.html'
    context_object_name = 'saved_login'
    model = UserSavedLogin
    form_class = SavedLoginForm
    success_url = reverse_lazy('pypass:list_login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = get_form_with_decrypted_password(context['form'])
        context['brand_icons_list'] = BrandIcon.objects.filter(is_activated=True)
        context["web_title"] = "Update"
        context['page_heading_title'] = "Update"
        return context

    def form_valid(self, form):
        plain_password = form.instance.password
        if plain_password:
            token_password = pwd_util.generate_password_token(plain_password)
            form.instance.password = token_password
        return super(PyPassUpdateLoginView, self).form_valid(form)


class PyPassDeleteLoginView(LoginRequiredMixin, DeleteView):
    login_url = 'pypass:login'
    redirect_field_name = 'redirect_to'
    model = UserSavedLogin
    success_url = reverse_lazy('pypass:list_login')
