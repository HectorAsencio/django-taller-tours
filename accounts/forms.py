from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tours.models import Usuario
from localflavor.cl.forms import CLRutField


class SignUpForm(UserCreationForm):
    rut = CLRutField()
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rut', 'first_name', 'last_name', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }))
