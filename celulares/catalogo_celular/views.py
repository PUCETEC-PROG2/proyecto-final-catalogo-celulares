
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import *

from .models import *

# from pokedex.forms import PokemonFor
# from .models import Pokemon
# from django.shortcuts import redirect, render

# #importacion de librearia de autenticacion 
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.decorators import login_required

def index(request):
   #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
   ## SELECT * FROM pokedex_pokemon ORD
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'index': index}, request))

def productos(request):
    productos = Producto.objects.order_by('categoria')
    #productos = Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request, 'productos.html', context)

#@login_required    
def agregar_producto(request):
    if request.method=='POST':
        form= ProductoForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
        
    else:   
        form = ProductoForm()
        
    return render(request,"productos_form.html",{'form': form }) 

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celular:productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos_form.html', {'form': form})

def eliminar_producto(required, id):
    producto = get_object_or_404(Producto, pk = id)
    producto.delete()
    return redirect('catalogo_celular:productos')

def compras(request):
    compras = Compra.objects.order_by('fecha_compra')
    #productos = Producto.objects.all()
    context = {
        'compras' : compras
    }
    return render(request, 'compras.html', context)

#@login_required    
def agregar_compra(request):
    if request.method=='POST':
        form= CompraForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celular:compras')
        
    else:   
        form = ProductoForm()
        
    return render(request,"compras_form.html",{'form': form }) 

#class CustomLoginView(LoginView):
#    template_name="login.html"
       

