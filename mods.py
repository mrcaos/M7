#######CREACION DE PYOYECTO#######

##par ver las versiones
#python -V --> ver version de python 
#python -m django ---> ver version de django

##crea el entorno
#python -m venv nombreEntorno

##activa el entorno
#source nombreEntorno/Scritpt/activate

##ver las dependencias
#pip list

##instalar dependencias DJANGO
#pip install django
#pip install django==3.2.4 ---> instala una version especifica

##instalar drivers de base de datos en nuestro entorno virtual 
#pip install psycopg2        #para postGres
#pip list

##respaldamos las instalaciones
#pip freeze > requirements.txt

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
##en una nueva terminal activaremos la base de datos postgreSQL
#psql -U postgres

##creacion de base de datos 
#create database nombre_baseDatos;

##entraremos a la base de datos creada
#\c nombre_baseDatos

##sqlite viene por defecto
#pip install psycopg2        #para postGres

#se reemplaza en settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "NOMBRE", #nombre de la base de datos que activaremos
        "USER": "postgres",
        "PASSWORD": "password", 
        "HOST": "127.0.0.1",
        "PORT": "5432", #segun el motor que ocuparemos
    }
}

#pip install mysqlclient      #para mysqlclient

##ejecutamos las migraciones
#python manage.py makemigrations
#python manage.py migrate

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
#crea un mejor entorno visual en el /admin
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


##Dumpdata
#obtener toda la data desde la base dato
python manage.py dumpdata --indent 2

python manage.py dumpdata --indent 2 rentApp

python manage.py dumpdata --indent 2 rentApp.region

python manage.py dumpdata --indent 2 rentApp.region > region.json

##Load Data
python manage.py loaddata region.json


##desplegar proyecto
#python manage.py runserver

#deactivate --> desactiva el entorno

