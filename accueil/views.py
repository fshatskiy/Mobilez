from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.

def Accueil_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'accueil/index.html')


def Inscription_view(request):
    # if there is data in the form that was sent = POST req
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # on récupère les données du form et on les sauvegarde dans 'user'
            user = form.save()
            # l'utilisateur se co
            login(request, user)
            return redirect('accueil')
    else:
        # if there is no data = GET req (envoie un form vide)
        form = UserCreationForm()
    # page qu'on va chercher lors de la requête
    return render(request, 'accueil/inscription.html', {
        'form': form
    })


def Connection_view(request):
    if request.method == 'POST':
        # on prend les données rentrées qui sont stockées mnt dans 'form' et on les vérifie
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # on récupère les données du form et on les sauvegarde dans la var 'user'
            user = form.get_user()
            # on le co
            login(request, user)
            return redirect('accueil')
    # GET request
    else:
        form = AuthenticationForm()
    return render(request, 'accueil', {
        'form': form
    })
