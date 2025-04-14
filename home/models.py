from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)