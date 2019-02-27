from django.db import models

class Banda(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)

class Album(models.Model):
    name = models.CharField(max_length=200)
    artista = models.ForeignKey(Banda, on_delete='DO_NOTHING')

class Integrantes(models.Model):
    name = models.CharField(max_length=200)
    instrumento = models.CharField(max_length=200)
    banda = models.ForeignKey(Banda, on_delete='CASCADE')
    # banda = models.ForeignKey(Banda, on_delete=CASCADE) 

