from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blogapp-home'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='blog_post_detail'),
    path('about/', views.about, name='blogapp-about'),
    path('create_post/', views.CreatePost.as_view(), name='blog-post-create'),
]

# views.home returns httpresponse o bject.
