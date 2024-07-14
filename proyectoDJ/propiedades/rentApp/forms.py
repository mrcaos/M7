from django import forms

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