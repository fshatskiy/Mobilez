from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', include('accueil.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('comptes.urls')),
]