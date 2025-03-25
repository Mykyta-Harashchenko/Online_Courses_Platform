from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'warrior'

urlpatterns = [
    path('add_warrior/', views.add_warrior, name='add_warrior'),
    path('<int:warrior_id>', views.warrior_detail, name='warrior_details'),
    path('warrior/<int:warrior_id>/add_comment/', views.add_comment, name='add_comment')
]