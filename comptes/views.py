from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def Inscription_view(request):
    # form = CreateUserForm()
    # if there is data in the form that was sent = POST req
    if request.method == 'POST':
        # stocker pseudo et mdp dans 'form'
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
    return render(request, 'comptes/inscription.html', {
        'form': form
    })


def Connexion_view(request):
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
    return render(request, 'comptes/connexion.html', {
        'form': form
    })
