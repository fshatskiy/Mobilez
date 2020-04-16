from django.urls import path, include
from accueil import views

urlpatterns = [
    # mobilez.be/
    path('', views.Accueil_view, name="accueil"),
    path('', views.Connection_view, name='connection'),
    # mobilez.be/inscription
    path('inscription/', views.Inscription_view, name='inscription'),
]