from django.contrib.auth.models import User
from djongo import models
from django import forms

# Création d'un formulaire perso
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
