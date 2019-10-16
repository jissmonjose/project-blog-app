from django.shortcuts import render, redirect
from .register import RegisterForm
from django import forms
# importing login requfred decorator before accesing profile page
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .register import UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    # create instance of form , if request is not posted or if posted.
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('usersapp:login')
    else:
        form = RegisterForm()
    return render(request, 'usersapp/register.html', {'form': form})


@login_required
def user_profile(request, template_name='usersapp/profile.html'):
    # v instantiate our forms as empty
    update_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    # later create context which key value pairs of that new isntance of form
    context = {
        'update_form': update_form, 'profile_form': profile_form
    }
    # pass that context to template
    return render(request, template_name, context)
