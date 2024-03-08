# api/models.py
from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ['id']  # Ordenar los resultados por id de forma creciente
