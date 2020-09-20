from django.db import models

# Create your models here.

class Gaseosa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
