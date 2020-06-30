from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from .models import NewsLetter, Partenaire, Presentation, Programme, SocialAccount 
from events.models import ActuEvent, Categorie, Contact, Lieu, Organisateur, Search, Tag, UserP, Ville 

# Create your views here.

def index(request):
    presentation = Presentation.objects.filter(status=True).last
    partenaire = Partenaire.objects.filter(status=True)[:10]
    programme = Programme.objects.filter(status=True)[:11]
    social_account = SocialAccount.objects.filter(status=True)[:5]

    data = {
        'presentation' : presentation,
        'partenaire' : partenaire,
        'programme' : programme,
        'social_account' : social_account,
    }
    
    return render(request, 'pages/index.html', data)


def contact(request):
    
    data = {
        
    }
    
    return render(request, 'pages/contact.html', data)     