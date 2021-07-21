from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from tours import views as login_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='accounts-login'),
    path('signup/', views.register, name='accounts-register')
]
