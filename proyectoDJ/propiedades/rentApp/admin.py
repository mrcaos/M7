from django.contrib import admin
from .models import Tipo_inmueble,Tipo_usuario,Usuario,Region,Comuna,Inmueble

# Register your models here.
admin.site.register(Tipo_inmueble)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','arrendada','tipo_inmueble','m2_construidos']
    
admin.site.register(Inmueble,InmuebleAdmin)