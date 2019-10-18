from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView


# Create your views here.
# function base views for listing
def home(request, template_name='blogapp/index.html'):
    return render(request, template_name, {'posts': Post.objects.all(), 'title': 'Home'})


# class based view for listing
class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    # to order the post from latest to oldest
    ordering = ['-date']


# details view
class PostDetails(DetailView):
    model = Post

# next once created the view, then map the urlpattern to this view.
# here v pass a queryset of POst to post key.


def about(request, template_name='blogapp/about.html'):
    return render(request, template_name, {'title': 'About'})
