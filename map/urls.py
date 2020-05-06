from django.urls import path, include
from accueil import views

urlpatterns = [
    # mobilez.be/
    path('map/', views.Map_view, name="map"),
]