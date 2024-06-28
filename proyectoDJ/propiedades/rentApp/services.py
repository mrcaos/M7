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