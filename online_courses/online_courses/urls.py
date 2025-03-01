from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_auth.urls')),
    path('warrior/', include('warrior.urls', namespace='warrior')),
    path('admin/', admin.site.urls),
]

# Для загрузки медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Для статических файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


