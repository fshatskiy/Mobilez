from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path
from account import views

urlpatterns = [
    # www.mobilez.be/inscription/
    path('inscription/', views.inscription_view, name='inscription'),
    # www.mobilez.be/connection/
    path('connection/', views.connection_view, name='connection'),
    # déconnexion
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
]