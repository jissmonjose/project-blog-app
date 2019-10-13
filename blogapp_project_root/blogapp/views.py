from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.

post = [
    {'author': 'Jacob John',
     'title': 'Blog Post 1',
     'content': 'First Post Content',
     'date': datetime.now(),
     },

    {'author': 'Remya Shivadas',
     'title': 'Blog Post 2',
     'content': 'Second Post Content',
     'date': datetime.now(),
     }
]


def home(request, template_name='blogapp/index.html'):
    return render(request, template_name, {'posts': Post.objects.all(), 'title': 'Home'})


# next once created the view, then map the urlpattern to this view.
# here v pass a queryset of POst to post key.




def about(request, template_name='blogapp/about.html'):
    return render(request, template_name, {'title': 'About'})
