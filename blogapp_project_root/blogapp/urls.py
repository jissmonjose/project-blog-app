from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blogapp-home'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='blog_post_detail'),
    path('about/', views.about, name='blogapp-about'),
]

# views.home returns httpresponse object.
