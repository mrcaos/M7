#agregar la logica de negocios para la aplicación
from .models import Tarea, SubTarea

#Dentro del archivo services.py crear 6 funciones:
def recupera_tareas_y_sub_tareas():
    lista_tareas = Tarea.objects.filter(eliminada= False)
    #lista_tareas = Tarea.objects.exclude(eliminada= True)
    arreglo_de_tareas = []

    for tarea in lista_tareas:
        subtareas = tarea.subtarea_set.filter(eliminada= False)
        dicc_tareas= {
            'tarea':tarea,
            'subtareas':subtareas
        }
        arreglo_de_tareas.append(dicc_tareas)

    return arreglo_de_tareas

def crear_nueva_tarea(pDescripcion='',pEliminada=False):
    tarea = Tarea(descripcion= pDescripcion, eliminada= pEliminada)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, pDescripcion='',pEliminada=False):
    tarea_fk= Tarea.objects.get(pk=tarea_id)
    print(tarea_fk)

    subtarea = SubTarea(descripcion= pDescripcion, eliminada= pEliminada,tarea=tarea_fk)
    subtarea.save()

    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.eliminada= True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    sub_tarea = SubTarea.objects.get(pk=subtarea_id)
    sub_tarea.eliminada= True
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla():
    pass