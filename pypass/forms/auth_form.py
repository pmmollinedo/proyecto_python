from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import TextInput, CharField, PasswordInput


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={
                'id': "loginInputUsername",
                'class': 'form-control form-control-user',
                'placeholder': 'Username'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'id': "loginInputPassword",
                'class': 'form-control form-control-user',
                'placeholder': 'Password'
            }
        )
    )
