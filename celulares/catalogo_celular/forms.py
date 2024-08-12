from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
           'nombre_producto' : forms.TextInput(attrs={'class' : 'form-control'}),
           'precio' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'marca' : forms.TextInput(attrs={'class' : 'form-control'}),
           'cantidad': forms.NumberInput(attrs={'class' : 'form-control'}),
           'procesador' : forms.Textarea(attrs={'class' : 'form-control'}),
           'pantalla' : forms.Textarea(attrs={'class' : 'form-control'}),
           'ram' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'camara' : forms.Textarea(attrs={'class' : 'form-control'}),
           'almacenamiento' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'categoria' : forms.Select(attrs={'class' : 'form-control'}),
           'imagen': forms.ClearableFileInput(attrs={'class' : 'form-control'}),
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
           'ciudad' : forms.TextInput(attrs={'class' : 'form-control'}),
           'fecha_compra' : forms.DateInput(attrs={'class' : 'form-control'}),
           'precio_total' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'cliente' : forms.Select(attrs={'class' : 'form-control'}),
           'productos' : forms.Select(attrs={'class' : 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
           'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
           'apellidos' : forms.TextInput(attrs={'class' : 'form-control'}),
           'cedula' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'telefono' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'correo' : forms.TextInput(attrs={'class' : 'form-control'}),
           
        }        