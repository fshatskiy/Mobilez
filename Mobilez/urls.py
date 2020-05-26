from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name="login"),
    path('', include('allauth.urls')),
    path('accueil/', include('accueil.urls')),
    path('map/', include('map.urls')),
]