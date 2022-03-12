from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ImageField, CharField

from pypass.models.profile import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'status': TextInput(
                attrs={
                    'id': 'formInputProfileStatus',
                    'class': 'form-control'
                }
            ),
            'avatar': TextInput(
                attrs={
                    'id': 'formInputProfileAvatar',
                    'class': 'd-none'
                }
            )
        }


class UserForm(ModelForm):
    password = CharField(
        widget=PasswordInput(
            attrs={
                'id': 'formInputProfilePassword',
                'class': 'form-control'
            }
        )
    )
    confirm_password = CharField(
        widget=PasswordInput(
            attrs={
                'id': 'formInputProfileConfirmPassword',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': TextInput(
                attrs={
                    'id': 'formInputProfileUsername',
                    'class': 'form-control'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'id': 'formInputProfileFirstName',
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'id': 'formInputProfileLastName',
                    'class': 'form-control'
                }
            ),
            'email': EmailInput(
                attrs={
                    'id': 'formInputProfileEmail',
                    'class': 'form-control'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
