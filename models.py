from django.db import models
from django.forms import IntegerField
class curso(models.Model):
      id= models.AutoField(primary_key=True)
      nombre= models.CharField(max_length=40)
      camada= models.IntegerField()
class estudiante(models.Model):
      nombre= models.CharField(max_length=40)
      apellido= models.CharField(max_length=40)
      email= models.EmailField()
class profesor(models.Model):
      nombre= models.CharField(max_length=40)
      apellido= models.CharField(max_length=40)
      email= models.EmailField()
      profesion= models.CharField(max_length=60)
class entregable(models.Model):
      nombre= models.CharField(max_length=40)
      fecha_de_entrega= models.DateField
      email= models.EmailField()
      entregado= models.BooleanField
      


