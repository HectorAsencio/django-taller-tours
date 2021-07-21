from django import forms
from django.contrib.auth.forms import UserCreationForm
from tours.models import Usuario
from localflavor.cl.forms import CLRutField


class SignUpForm(UserCreationForm):
    rut = CLRutField()
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rut', 'first_name', 'last_name', 'password1', 'password2']
