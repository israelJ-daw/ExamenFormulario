from django.db import models
from time import timezone 

# Create your models here.

class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    puede_tener_promociones = models.BooleanField()

    def __str__(self):
        return self.nombre


class promocion(models.Model):
    nombre= models.CharField(max_length=100, unique=True)
    descripcion=models.CharField(max_length=100, null=True)
    puede_tener_promociones = models.BooleanField(null=True)
    usuarios_aplicable=models.CharField(max_length=100)
    descuento=models.IntegerField(null=True)
    fecha_inicio= models.DateTimeField()
    fecha_fin= models.DateTimeField()
    activa=models.BooleanField()
    
    

