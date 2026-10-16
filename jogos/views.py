from django.shortcuts import render
from .models import Equipe, Atleta, Modalidade, Tecnico

# Create your views here.
def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, "jogos/index.html", {'equipes': equipes, 'modalidades': modalidades})

def equipe(request):
    return render(request, "jogos/equipe.html")

def modalidade(request):
    return render(request, "jogos/modalidade.html")