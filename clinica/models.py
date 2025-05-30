from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)

class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='medicos/', blank=True, null=True)

    def __str__(self):
        return f' {self.nombre} - {self.apellido}'