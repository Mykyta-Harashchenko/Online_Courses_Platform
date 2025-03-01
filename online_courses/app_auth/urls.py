from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include

from . import views
from .forms import LoginForm

app_name = 'app_auth'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('signin/', LoginView.as_view(template_name='app_auth/registration/login.html', form_class=LoginForm), name='signin'),
    path('logout/', views.logoutuser, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='app_auth/registration/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='app_auth/registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='app_auth/registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='app_auth/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
]