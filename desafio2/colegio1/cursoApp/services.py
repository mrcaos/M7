from .models import Curso,Profesor,Estudiante,Direccion

def crear_curso(Curso,Nombre,Version):
    #crear instancia
    curso=Curso(codigo=Curso,nombre=Nombre,version=Version)
    #guardar la instancia
    curso.save()
    return curso

def crear_profesor(Rut,Nombre,Apellido,Creado):
    #crear instancia
    profe=Profesor(rut=Rut,nombre=Nombre,apellidos=Apellidos,creado_por=Creado)
    #guardar instancia
    profe.save()
    return profe

def crear_estudiante(Rut,Nombre,Apellido,Fecha,Creado):
    estudiante=Estudiante(rut=Rut,nombre=Nombre,apellidos=Apellido,creado_por=Creado,fecha_nacimiento=Fecha)
    estudiante.save()
    return estudiante

def crear_direccion(estudiante,Calle,Numero,Dpto,Comuna,Ciudad,Region):
    direccion=Direccion(estudiante=estudiante,calle=Calle,numero=Numero,dpto=Dpto,comuna=Comuna,ciudad=Ciudad,reion=Region)
    direccion.save()
    return direccion

def obtiene_estudiante(Rut):
    #est=Estudiante.objects.get(rut=Rut)
    #est=Estudiante.objects.get(pk=Rut)
    #return est
    return Estudiante.objects.get(pk=Rut)

def obtiene_profesor(Rut):
    return Profesor.objects.get(pk=Rut)

def obtiene_curso():
    pass

def agrega_profesor_a_curso(Curso,Profesor):
    Profesor.cursos.add(Curso)

def agrega_cursos_a_estudiante(estudiante,curso):
    estudiante.curso.add(Curso)

def imprime_estudiante_cursos():
    pass 