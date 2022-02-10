from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea, CheckboxInput

from pypass.models.user_logins import UserSavedLogins


class CreateSavedLoginForm(ModelForm):

    class Meta:
        model = UserSavedLogins
        exclude = ['app_user']
        labels = {
            'username': 'Username'
        }
        widgets = {
            'sitename': TextInput(
                attrs={
                    'id': "formInputSiteName",
                    'class': 'form-control',
                    'placeholder': 'SiteName'
                }
            ),
            'brand_icon': TextInput(),
            'username': TextInput(
                attrs={
                    'id': "formInputUserName",
                    'class': 'form-control',
                    'placeholder': 'Username'
                }
            ),
            'email': EmailInput(
                attrs={
                    'id': "formInputEmail",
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'id': "formInputPassword",
                    'class': 'form-control',
                    'placeholder': 'Password'
                }
            ),
            'notes': Textarea(
                attrs={
                    'id': "formInputNotes",
                    'class': 'form-control',
                    'placeholder': 'Write something...',
                    'rows': '4'
                }
            ),
            'is_fav': CheckboxInput(
                attrs={
                    'id': "formInputFavCheckbox",
                    'class': 'd-none'
                }
            )
        }


class UpdateSavedLoginForm(ModelForm):

    class Meta:
        model = UserSavedLogins
        exclude = ['app_user']
        labels = {
            'username': 'Username'
        }
        widgets = {
            'sitename': TextInput(
                attrs={
                    'id': "formInputSiteName",
                    'class': 'form-control',
                    'placeholder': 'SiteName'
                }
            ),
            'brand_icon': TextInput(),
            'username': TextInput(
                attrs={
                    'id': "formInputUserName",
                    'class': 'form-control',
                    'placeholder': 'Username'
                }
            ),
            'email': EmailInput(
                attrs={
                    'id': "formInputEmail",
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'id': "formInputPassword",
                    'class': 'form-control',
                    'placeholder': 'Password'
                }
            ),
            'notes': Textarea(
                attrs={
                    'id': "formInputNotes",
                    'class': 'form-control',
                    'placeholder': 'Write something...',
                    'rows': '4'
                }
            ),
            'is_fav': CheckboxInput(
                attrs={
                    'id': "formInputFavCheckbox",
                    'class': 'd-none'
                }
            )
        }
