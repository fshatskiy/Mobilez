from django.urls import path, include
from map import views

urlpatterns = [
    # mobilez.be/
    path('', views.Map_view, name="map"),
]