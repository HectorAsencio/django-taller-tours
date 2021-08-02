from accounts.forms import UserLoginForm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='accounts-login'),
    path('signup/', views.register, name='accounts-register')
]
