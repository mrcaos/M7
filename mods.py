"""
#######CREACION DE PYOYECTO#######

python -m venv nombreEntorno

source nombreEntorno/Scritpt/activate

python -V --> ver version de python 
python -m django ---> ver version de django

pip install django
pip install django==3.2.4 ---> instala una version especifica

pip list ---> ver versiones instaladas

django-admin startproject nombreProyecto
cd nombreProyecto

python manage.py startapp nombreApp ---> creamos una aplicacion
setting.py
agregar la aplicacion en el settings.py 
INSTALLED_APPS = [
    'nombreApp',
]

python manage.py migrate
python manage.py createsuperuser --> creamos el super usuario, en la web /admin
python manage.py runserver

deactivate --> desactiva el entorno 


########CREACION DE MODELOS#######

en models.py crearemos un modelo de contenga varios atributos 
los models dependeran de lo pedido por el cliente

from django.db import models 

# Create your models here.

class Tarea(models.Models):
class Flan(models.Model):


#######ORM#######
instalar drivers de bse de datos, se pueden instalar varios sin problema 

se reemplaza en settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sistema_base",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "5432", #segun el motor que ocuparemos
    }
}

pip install psycopg2   #postgres
pip list
pip install mysqlclient

python manage.py makemigrations
python manage.py migrate

#conocer todas las migraaciones y saber cuales se han ejecutado
python manage.py showmigrations 

revertir una aplicacion especifica
python manage.py migrate testadl 0001_initial

revierte todas las migraciones de una aplicacion 
python manage.py migrate testadl zero

terminal conectada a la base de datos
python manage.py shell
"""