from django.shortcuts import render, get_object_or_404
from .models import Equipe, Atleta, Modalidade, Tecnico

# Create your views here.
def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, "jogos/index.html", {'equipes': equipes, 'modalidades': modalidades})

def equipe(request, id):
    equipe = get_object_or_404(
        Equipe,
        id=id
    )

    return render(request, "jogos/equipe.html", {'equipe': equipe})

def modalidade(request):
    return render(request, "jogos/modalidade.html")