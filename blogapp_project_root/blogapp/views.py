from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Post
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView, )
from django.contrib.auth.models import User


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
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(title__icontains=query)
        else:
            posts = self.model.objects.all()
        return posts


# details view
class PostDetails(DetailView):
    model = Post


# creating new posts
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update view

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False


# delete post
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp-home')

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False


# filter posts based on author
class UserPostView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blogapp/user_posts.html'
    paginate_by = 4

    def get_queryset(self):
        # v try to get the user when v click link on author name in post list
        # to get that user object v do self.kwargs.get('username')
        # self.kwargs is a dictionary of that user datas, and v use get method to fetch username of that user from that dictionary
        # here if user exists in User model v store it in user variable else, return 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # now filter the post list based on author and order it by date.
        return Post.objects.filter(author=user).order_by('-date')


def about(request, template_name='blogapp/about.html'):
    return render(request, template_name, {'title': 'About'})
