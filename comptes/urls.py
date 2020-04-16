from django.urls import path, include

from comptes import views

urlpatterns = [
    # mobilez.be/connexion/
    path('', views.Connexion_view, name='connexion'),
    # mobilez.be/inscription/
    path('inscription/', views.Inscription_view, name='inscription'),
]