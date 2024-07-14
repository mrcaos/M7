from django import forms

class LoginForm(forms.Form):
    #username = forms.CharField(max_length=64,label='Nombre')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.PasswordInput()

class InmuebleForm(forms.Form):
    nombre=forms.CharField(label='Nombre',max_length=50)
    descripcion=forms.CharField(label='Descripcion')
    m2_construidos=forms.FloatField(label='Construidos')
    m2_terreno=forms.FloatField(label='Metros Terreno')
    num_estacionamiento=forms.IntegerField(label='Num Est')
    num_habitaciones=forms.IntegerField(label='Num Habt')
    num_banios=forms.IntegerField(label='Num Ba')
    direccion=forms.CharField(label='Direccion',max_length=50)
    precio_mensual=forms.FloatField(label='Precio')
    
class UsuarioForm(forms.Form):
    rut = forms.CharField(label='Rut', max_length=12)
    direccion=forms.CharField(label='Direccion',max_length=50)
    telefono=forms.CharField(label='Telefono',max_length=50)