from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('accueil/', include('accueil.urls')),
    path('map/', include('map.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)