from django.urls import path, include

from accueil import views

urlpatterns = [
    # www.mobilez.be/
    path('', views.accueil_view, name="accueil"),
]