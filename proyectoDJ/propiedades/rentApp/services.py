from .models import Tipo_inmueble,Tipo_usuario,Usuario,Region,Comuna,Inmueble

def get_all_inmuebles():
    lista_inmuebles=Inmueble.objects.all()
    return lista_inmuebles

def save_inmueble(data):
    comuna=Comuna.object.get(pk=data[9])
    
    Inmueble=Inmueble(nombre=data[0],
                    comuna=comuna)
    
    inmueble.save()
    

def elim(inmueble_id):
    Inmueble.objects.get(pk=inmueble_id).delete()
    
def get_orm_inmuebles(nombre,descripcion):
    inmuebles = Inmueble.objects.filter(nombre__contains=nombre)
    if descripcion is not None:
        inmuebles = inmuebles.filter(descripcion__contains=descripcion)
        
    archivo =open('propiedades_nombre_desc.txt', 'w')

    for inmu in inmuebles:

        archivo.write(inmu.nombre+' - '+inmu.descripcion+'\n')
    
    archivo.close()
        
        
def get_raw_inmuebles(comuna_nombre):
    query = """
            select inmu.id, inmu.nombre, inmu.descripcion, comu.nombre as comuna, reg.nombre as region    
            from miapp_inmueble inmu
            inner join miapp_comuna comu
            ON inmu.comuna_id = comu.id
            inner join miapp_region reg
            ON inmu.region_id = reg.id
            where comu.nombre like '%"""+ str(comuna_nombre)+ """%' """
            #where comu.id = 1

    inmuebles = Inmueble.objects.raw(query)

    archivo =open('propiedades_x_comuna.txt', 'w')

    for inmu in inmuebles:

        archivo.write(inmu.nombre+' - '+inmu.descripcion+'\n')
    
    archivo.close()
    
    
def get_region_inmuebles():
    regiones= Region.objects.all()
    lista_inmuebles = Inmuebles.objects.all()
    for reg in regiones:
        inmuebles = Inmueble.objects.filter(region= reg)
        for inmu in lista_inmuebles:
            reg.id == lista_inmuebles.region.id