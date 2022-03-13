from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, CharField, PasswordInput, EmailField, EmailInput

from pypass.models.profile import Profile


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


class RegisterForm(UserCreationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'id': 'registerInputUsername',
                'class': 'form-control form-control-user',
                'placeholder': 'Username'
            }
        )
    )
    first_name = CharField(
        widget=TextInput(
            attrs={
                'id': 'registerInputFirstName',
                'class': 'form-control form-control-user',
                'placeholder': 'First Name'
            }
        )
    )
    last_name = CharField(
        widget=TextInput(
            attrs={
                'id': 'registerInputLastName',
                'class': 'form-control form-control-user',
                'placeholder': 'Last Name'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'id': 'registerInputEmail',
                'class': 'form-control form-control-user',
                'placeholder': 'Email Address'
            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'id': "registerInputPassword",
                'class': 'form-control form-control-user',
                'placeholder': 'Password'
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'id': "registerInputConfirmPassword",
                'class': 'form-control form-control-user',
                'placeholder': 'Confirm Password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User already exists.")
        return username

    def clean_password2(self):
        password = self.cleaned_data['password1']
        confirm_password = self.cleaned_data['password2']
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords don't match")
        return password

    def save(self, commit=True):
        username = self.cleaned_data['username']
        user = User.objects.create_user(
            username,
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        Profile.objects.create(user=user, avatar="default_profile_1.svg", status="Chilling.")
        return user
