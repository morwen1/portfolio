from django.db import models

# Create your models here.
class Datos (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero = models.CharField(max_length=11)
