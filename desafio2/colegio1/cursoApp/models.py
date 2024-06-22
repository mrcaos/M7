from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    version=models.IntegerField()
    
class Profesor(models.Model):
    rut=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    apellidos=models.CharField(max_length=50,null=False,blank=False)
    activo=models.BooleanField(default=False)
    creado_por=models.CharField(max_length=50)
    #ManyToMany
    curso=models.ManyToManyField('curso',related_name='profesores')
    creacion_registro=models.DateTimeField(auto_now_add=True)
    modificacion_registro=models.DateTimeField(auto_now=True)
    
class Estudiante(models.Model):
    rut=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    apellidos=models.CharField(max_length=50,null=False,blank=False)
    fecha_nacimiento=models.DateTimeField(null=False,blank=False)
    activo=models.BooleanField(default=False)
    creacion_registro=models.DateTimeField(auto_now_add=True)
    modificacion_registro=models.DateTimeField(auto_now=True)
    creado_por=models.CharField(max_length=50)
    curso=models.ForeignKey(Curso,related_name='estudiantes',on_delete=models.CASCADE)

class Direccion(models.Model):
    calle=models.CharField(max_length=50, null=False, blank=False)
    numero=models.CharField(max_length=10, null=False, blank=False)
    depto=models.CharField(max_length=10, null=True)
    comuna=models.CharField(max_length=50, null=False, blank=False)
    ciudad=models.CharField(max_length=50, null=False, blank=False)
    region=models.CharField(max_length=50, null=False, blank=False)
    estudiante=models.OneToOneField('Estudiante',related_name='direccion',on_delete=models.CASCADE)