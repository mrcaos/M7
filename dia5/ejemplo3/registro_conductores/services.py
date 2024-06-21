from .models import Conductor,Direccion,Vehiculo

def crear_conductor(pRut,pNombre,pApellido,pFecha):
    conductor = Conductor(rut=pRut, nombre=pNombre, apellido=pApellido, fecha_nacimiento=pFecha)
    conductor.save()
    imprimir_modelos()

def agregar_direccion_a_conductor(pCalle,pNumero,pDepto,pComuna,pRegion,conductor_rut):
    obj_conductor = Conductor.objects.get(pk=conductor_rut)
    
    direccion = Direccion(calle=pCalle,numero=pNumero,depto=pDepto,comuna=pComuna,region=pRegion,conductor=obj_conductor,ciudad=pCiudad)
    direccion.save()
    imprimir_modelos()

def agregar_un_vehiculo(pPatente,pMarca,pModelo,pYear,conductor_rut):
    obj_conductor = Conductor.objects.get(pk=conductor_rut)
    
    vehiculo = Vehiculo(patente=pPatente,marca=pMarca,modelo=pModelo,year=pYear,conductor=obj_conductor)
    imprimir_modelos()

def eliminar_vehiculo(vehiculo_id): 
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    vehiculo.delete()#borrado fisico
    imprimir_modelos()

def eliminar_conductor(rut):
    obj_conductor = Conductor.objects.get(pk=rut)
    obj_conductor.delete()
    imprimir_modelos()

def imprimir_modelos():
    lista_conductores= Conductor.objects.all()
    
    for conductor in lista_conductores:
        print(f"{conductor.rut} - {conductor.nombre} - {conductor.apellido} - {conductor.fecha_nacimiento}")
        print(f"{conductor.direccion.calle} {conductor.direccion.numero} {conductor.direccion.depto}...")
        #print(conductor.vehiculo)
        vehiculos = conductor.vehiculo_set.all()
        for ve in vehiculos:
            print(f"{ve.patente}-{ve.marca}, {ve.modelo}, {ve.year}")