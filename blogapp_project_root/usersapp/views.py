from django.shortcuts import render, redirect
from .register import RegisterForm
from django import forms
from django.contrib import messages


# Create your views here.
def register(request):
    # create instance of form , if request is not posted or if posted.
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blogapp-home')
    else:
        form = RegisterForm()
    return render(request, 'usersapp/register.html', {'form': form})
