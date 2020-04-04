from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# pour permettre aux users de se co
from django.contrib.auth import login, logout


# Create your views here.

def inscription_view(request):
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
    return render(request, 'account/inscription.html', {
        'form': form
    })


def connection_view(request):
    if request.method == 'POST':
        # on prend les données rentrées qui sont stockées mnt dans 'form' et on les vérifie
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # on récupère les données du form et on les sauvegarde dans 'user'
            user = form.get_user()
            # on le co
            login(request, user)
            return redirect('accueil')
    # GET request
    else:
        form = AuthenticationForm()
    return render(request, 'account/connection.html', {
        'form': form
    })

def deconnexion_view(request):
    if request.method == 'POST':
        # django already knows that we are logged in : log current user out
        logout(request)
        return redirect('accueil')