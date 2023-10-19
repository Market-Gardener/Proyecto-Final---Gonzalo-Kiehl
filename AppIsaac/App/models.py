from django.db import models

# Create your models here.
class Objeto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    tipoMoneda = models.CharField(max_length=20)
    tipo = models.CharField(max_length=40)

class Item(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    personaje = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

