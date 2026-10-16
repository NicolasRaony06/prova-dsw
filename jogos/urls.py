from django.urls import path
from .views import *

app_name = 'jogos'

urlpatterns = [
    path('', index, name="index"),
    path('equipes/<int:id>/', equipe, name="equipe"),
    path('modalidades/<int:id>/', modalidade, name="modalidade") 
]
