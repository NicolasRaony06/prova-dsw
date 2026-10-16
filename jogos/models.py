from django.db import models

# Create your models here.
class Modalidade(models.Model):
    class Tipo(models.TextChoices):
        COLETIVO = 'Coletivo'
        INDIVIDUAL = 'Individual'

    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(choices=Tipo)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    criada_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=50)
    equipe = models.OneToOneField("Equipe", on_delete=models.CASCADE, related_name='tecnico')

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        ordering = ['nome']

    def __str__(self):
        return self.nome    

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey("Equipe", on_delete=models.PROTECT, related_name='atletas')
    modalidades = models.ManyToManyField("Modalidade", null=True, blank=True, related_name='atletas')

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'
        ordering = ['nome']

    def __str__(self):
        return self.nome        

    