from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


def register(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, f'Se ha registrado de forma exitosa.')
            return redirect('accounts-login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
