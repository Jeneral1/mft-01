from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="Bloghome"),

    path('login/', auth_views.LoginView.as_view(template_name='move/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='move/password_reset.html'), name='password_reset'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_post, name='create_post'),
]