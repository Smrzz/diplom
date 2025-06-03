from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('news', include('news.urls')),
    path('hostels', include('hostels.urls')),
    path('rental', include('rental.urls')),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=(settings.MEDIA_ROOT),
    )

