from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pessoa (models.Model):

    CPF    = models.IntegerField()
    Nome = models.CharField(max_length=200)
    EMail = models.EmailField()
    Data_Nascimento = models.DateField()
    Data_Cadastro = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):

        return self.nom_pessoa

class Evento(models.Model):

    nome = models.CharField(max_length=200)
    data = models.DateTimeField()
    local = models.CharField(max_length=200)

    def __unicode__(self):

        return self.nome

class Imagem(models.Model):

    evento = models.ForeignKey(Evento)
    legenda = models.CharField(max_length=200)
    foto= models.ImageField(upload_to='images')

    def __unicode__(self):

        return self.legenda
