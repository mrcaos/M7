from django.shortcuts import render,redirect
from .models import Tipo_inmueble, Inmueble, Usuario, Tipo_usuario
from .forms import InmuebleForm,LoginForm,UsuarioForm
from django.views.generic import ListView

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def registro(request):
    if request.method =="GET":#desplegar el HTML
        return render(request,"registro.html")
    
    if request.method =="POST": #CAPTURA Y GUARDA LOS DATOS 
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pass"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        
        user = User.objects.create_user(username, email, password)
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        
        return redirect("login")
        
        ###USUARIO###
        rut = request.POST["rut"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        ##Tipo usuario arrendatario = 2
        tipo_usuario = Tipo_usuario.objects.get(pk=2)
        usuario = Usuario(user=user,rut=rut,direccion=direccion,telefono=telefono,tipo_usuario=tipo_usuario)
        usuario.save()

    
class SignUpView(CreateView):
    form_class = LoginForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    
    context={
        'tipo_usuario':request.user.usuario.tipo_usuario.id,
        'tipo_inmuebles':Tipo_inmueble.objects.all()
    }
    
    return render(request,'index.html',context)

class InmuebleListView(ListView):
    model = Inmueble
    context_object_name = 'lista_inmuebles'   # su propio nombre para la lista como variable de plantilla
    template_name = 'propiedades.html'  # Especifique su propio nombre/ubicación de plantilla
    paginate_by = 1
    
def mispropiedades(request):
    lista_inmuebles = Inmueble.objects.all()
    context={
        'form':InmuebleForm(),
        'lista_inmuebles':lista_inmuebles
    }
    return render(request,'mispropiedades.html',context)


def actualizar_usuario(request):
    if request.method == "POST":
        u_form = UsuarioForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/')
    else:
        u_form = UsuarioForm(instance=request.usuario.profile)
        context={'u_form': u_form}
        return render(request, 'usuario_actualizar.html',context)