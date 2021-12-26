from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/profiles/', include('profiles.urls')),
    path('api/accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
