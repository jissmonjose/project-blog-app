from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Post
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)


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


# creating new posts
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request, template_name='blogapp/about.html'):
    return render(request, template_name, {'title': 'About'})
