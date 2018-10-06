from django.db import models
# Create your models here.
class Contacto (models.Model):
    email = models.EmailField()