from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    context = {

    }
    return render(request, 'win/index.html', context)

def players(request):
    player_list = Player.objects.all()
    context = {
        'player_list': player_list
    }
    return render(request, 'win/player.html', context)