from django.shortcuts import render
from .models import Sportsgame 


# Create your views here.

def index(request):

    context = {
        'sportsdata' : list(Sportsgame.objects.values())
    }


    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html')

def games(request):
    return render(request, 'games.html')

def about(request):
    return render(request, 'about.html')

def trainer(request):
    return render(request, 'trainer.html')