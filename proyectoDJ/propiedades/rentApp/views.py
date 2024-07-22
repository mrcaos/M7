import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Tipo_inmueble, Inmueble, Usuario,Tipo_usuario,Region,Comuna
from .forms import InmuebleForm,LoginForm,UsuarioForm
from django.views.generic import ListView
from django.views import generic

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def registro(request):
    if request.method =="GET":#desplegar el html
        return render(request,"registro.html")

    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pass"]

        user = User.objects.create_user(username, email, password)
        print(user)
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        user.first_name = nombre
        user.last_name = apellido
        user.save()

        ##### Usuario ###
        rut = request.POST["rut"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        #tipo usuario arrendatario = 2
        tipo_usuario = Tipo_usuario.objects.get(pk=2)
        usuario = Usuario(user =user, rut=rut,direccion =direccion,telefono = telefono,tipo_usuario= tipo_usuario)
        usuario.save()

        return redirect("login")

def actualizar_usuario(request):
    if request.method == 'POST':
        u_form = UsuarioForm(request.POST,instance=request.user.usuario)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/')
    else:
        u_form = UsuarioForm(instance=request.user.usuario)
        context={'u_form': u_form}
        return render(request, 'usuario_actualizar.html',context )

class SignUpView(CreateView):
    form_class = LoginForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    
    context={
        #'tipo_usuario':request.user.usuario.tipo_usuario.id,
        'lista_inmuebles': Inmueble.objects.values(),
        'tipo_inmuebles':Tipo_inmueble.objects.all(),
        'regiones': Region.objects.all(), 
    }

    return render(request,'index.html', context)


class InmuebleListView(ListView):
    model = Inmueble
    context_object_name = 'lista_inmuebles'   # su propio nombre para la lista como variable de plantilla
    template_name = 'propiedades.html'  # Especifique su propio nombre/ubicación de plantilla
    paginate_by = 1

def mispropiedades(request):
    lista_inmuebles = Inmueble.objects.all()
    context={
        'form': InmuebleForm(),
        'lista_inmuebles':lista_inmuebles
    }
    return render(request,'mispropiedades.html',context)

class InmuebleCreateView(generic.CreateView):
    model = Inmueble
    form_class = InmuebleForm
    success_url = "/"
    template_name = 'mispropiedades.html'

    def form_valid(self, form):
        inmueble= form.save(commit=False)
        inmueble.arrendador = self.request.user
        inmueble.save()

        return super().form_valid(form)
    

def filtrar_comunas(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            regionId = data.get('regionId')
            print('**** region id ****',regionId)
            dataBD = list(Comuna.objects.filter(
                region=regionId).values()
                )
            print('**** dataBD ****',dataBD)
            return JsonResponse({'status': 200, 'data': dataBD})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    
def inmuebles_buscar(request):
    return render(request,'formulario_busqueda.html',context)

