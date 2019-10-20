from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blogapp-home'),
    path('<str:username>/', views.UserPostView.as_view(), name='users_blog'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='blog_post_detail'),
    path('about/', views.about, name='blogapp-about'),
    path('post/create/', views.CreatePost.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='blog-post-delete'),
]

# views.home returns httpresponse object.
