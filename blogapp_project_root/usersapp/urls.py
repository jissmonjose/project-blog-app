from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usersapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name='logout'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='usersapp/password_reset.html'),
         name='password_reset'),
    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='usersapp/password_reset_done.html'),
         name='password_reset_done'),
    path('', include('blogapp.urls')),

]
