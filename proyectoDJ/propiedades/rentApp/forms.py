from django import forms
#from django_select2 import forms as s2forms
from .models import Usuario, Inmueble

class LoginForm(forms.Form):
    #username = forms.CharField(max_length=64,label='Nombre')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.PasswordInput()

class InmuebleForm(forms.ModelForm):
    class Meta:
        model=Inmueble 
        fields=['nombre','descripcion','m2_construidos','m2_terreno','num_estacionamiento',
                'num_habitaciones','num_banios','direccion','precio_mensual']        
        Widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':2, 'cols':10}),
            'm2_construidos':forms.NumberInput(attrs={'class':'form-control','min':0, 'max':1000,'value':0}),
            'm2_terreno':forms.NumberInput(attrs={'class':'form-control','min':0, 'max':1000,'value':0}),
            'num_estacionamiento':forms.NumberInput(attrs={'class':'form-control','min':0, 'max':100,'value':0}),
            'num_habitaciones':forms.NumberInput(attrs={'class':'form-control','min':0, 'max':100,'value':0}),
            'num_banios':forms.NumberInput(attrs={'class':'form-control','min':0, 'max':200,'value':0}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder': 'direccion'}),
            'precio_mensual':forms.NumberInput(attrs={'class':'form-control','min':0,'value':0}),
        }
    
class UsuarioForm(forms.ModelForm):
    rut = forms.CharField(label='Rut', max_length=12)
    direccion=forms.CharField(label='Direccion',max_length=50)
    telefono=forms.CharField(label='Telefono',max_length=50)
    class Meta:
        model = Usuario
        fields = ['rut','direccion','telefono']
        