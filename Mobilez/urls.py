from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accueil.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
