from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'app_auth'

urlpatterns = [
    path('', views.main, name='root'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('signin/', LoginView.as_view(template_name='app_auth/registration/login.html', form_class=LoginForm), name='signin'),
]