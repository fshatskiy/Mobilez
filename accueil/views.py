from django.shortcuts import render, redirect


# Create your views here.

def Accueil_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'accueil/index.html')