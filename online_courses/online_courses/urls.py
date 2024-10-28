from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_auth.urls')),
    path('admin/', admin.site.urls),
]
