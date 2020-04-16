from django.urls import path, include
from accueil import views

urlpatterns = [
    # mobilez.be/
    path('', views.Accueil_view, name="accueil"),
]