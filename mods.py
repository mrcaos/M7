#######CREACION DE PYOYECTO#######

##par ver las versiones
#python -V --> ver version de python 
#python -m django ---> ver version de django

##crea y activa el entorno
#python -m venv nombreEntorno
#source nombreEntorno/Scritpt/activate

##ver las dependencias e instalar lo solicitado
#pip list
#pip install django
#pip install django==3.2.4 ---> instala una version especifica
#pip list

##crear proyecto e ingresar a la carpeta
#django-admin startproject nombreProyecto
#cd nombreProyecto

##agregar App al proyecto 
#python manage.py startapp nombreApp

##vinculamos App al proyecto (setting.py)
INSTALLED_APPS = [
    'nombreApp',
    ...,
]

##ORM instalar driver en nuestro entorno virtual 
#sqlite viene por defecto
#pip install psycopg2        #para postGres
#se reemplaza en settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sistema_base",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432", #segun el motor que ocuparemos
    }
}
#pip install mysqlclient      #para mysqlclient

##insertar/crear super usuario
#python manage.py createsuperuser

##CREACION DE MODELOS
#crear el modelo en models.py
#from django.db import models
class Tarea(models.Model):
    pass

class Flan(models.Model):
    pass
##ejecutamos las migraciones
#python manage.py makemigrations
#python manage.py migrate

##en la App creamos el archivo 
#services.py
#importamos los modelos/agregamos los metodos 
from .models import Tarea,Flan

def metodo_requerido():
    pass

######TEMPLATES######
#crear carpeta templates en la App
#crear los HTML, con estrutura basica
#crear metodo de despliegue en HTML
#crear ruta que enlaza a views.py de la App

## Jazzmin
#pip install -U django-jazzmin
INSTALLED_APPS = [
    'jazzmin',
    ...,
]

#python manage.py runserver 0.0.0.0:8000
#http://192.168.0.17:8000

##conocer todas las migraaciones y saber cuales se han ejecutado en la base de datos
#python manage.py showmigrations 
#python manage.py showmigrations testadl

##revertir migracion especifica
#python manage.py migrate testadl 0001_initial

##revierte todas las migraciones de una aplicacion 
#python manage.py migrate testadl zero

##terminal conectada a la base de datos
#python manage.py shell

##desplegar proyeco
#python manage.py runserver

#deactivate --> desactiva el entorno 