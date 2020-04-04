from django.shortcuts import render


# Create your views here.

def accueil_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'accueil/index.html')
