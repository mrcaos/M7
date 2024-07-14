from django.shortcuts import render
from .models import Tipo_inmueble, Inmueble
from .forms import InmuebleForm
from django.views.generic import ListView

# Create your views here.
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