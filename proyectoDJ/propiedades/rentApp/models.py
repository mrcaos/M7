from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo_usuario(models.Model):
    nombre=models.CharField(max_length=12)

class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=False)
    rut=models.CharField(max_length=9,primary_key=True)
    nombres=models.CharField(max_length=50,null=False,blank=False)
    apellidos=models.CharField(max_length=50,null=False,blank=False)
    direccion=models.CharField(max_length=50,null=False,blank=False)
    telefono=models.CharField(max_length=50,null=False,blank=False)
    correo=models.CharField(max_length=50,null=False,blank=False)
    tipo_usuario=models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE,null=False)

class Tipo_inmueble(models.Model):
    nombre=models.CharField(max_length=15)

class Region(models.Model):
    nombre=models.CharField(max_length=25)

class Comuna(models.Model):
    nombre=models.CharField(max_length=25)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,null=False)

class Inmueble(models.Model):
    nombre=models.CharField(max_length=50,null=False,blank=False)
    descripcion=models.TextField()
    m2_construidos=models.FloatField(null=False)
    m2_terreno=models.FloatField(null=False)
    num_estacionamiento=models.IntegerField(default=0)
    num_habitaciones=models.IntegerField(default=0)
    num_banios=models.IntegerField(default=0)
    direccion=models.CharField(max_length=50,null=False,blank=False)
    precio_mensual=models.FloatField(null=False)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE,null=False)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,null=False)
    tipo_inmueble=models.ForeignKey(Tipo_inmueble,on_delete=models.CASCADE,null=False)
    arrendador=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    arrendatario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    arrendada=models.BooleanField(default=False)