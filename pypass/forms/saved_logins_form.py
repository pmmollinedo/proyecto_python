from django.forms import ModelForm, TextInput,  Select, EmailInput, PasswordInput, Textarea, CheckboxInput
from pypass.models.user_logins import UserSavedLogin


class SavedLoginForm(ModelForm):

    class Meta:
        model = UserSavedLogin
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
            'brand_icon': Select(
                attrs={
                    'id': "brand_icon_select",
                    'class': 'd-none'
                }
            ),
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
                    'placeholder': 'Password',
                    'maxlength': '50'
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

    def __init__(self, *args, **kwargs):
        super(SavedLoginForm, self).__init__(*args, **kwargs)
        self.fields['brand_icon'].empty_label = None

