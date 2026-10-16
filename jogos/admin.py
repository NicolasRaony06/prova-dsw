from django.contrib import admin
from .models import Atleta, Modalidade, Equipe, Tecnico

# Register your models here.
class TecnicoInline(admin.TabularInline):
    model = Tecnico

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe__nome', 'modalidades']
    search_fields = ['nome']

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display= ['nome', 'curso'] #fazer quantidades de atletas
    inlines = [TecnicoInline]

admin.site.register(Modalidade)
admin.site.register(Tecnico)