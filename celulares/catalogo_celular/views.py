
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import *

from .models import *

# from pokedex.forms import PokemonFor
# from .models import Pokemon
from django.shortcuts import redirect, render

# #importacion de librearia de autenticacion 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

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

def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)
    context = {
        'producto': producto
    }
    return render(request, 'detalle_producto.html', context)

def views_productos(request):
    
    producto = Producto.objects
    context = {
        'producto': producto 
    }
    return render(request, 'views_productos.html', context)



#@login_required    
def agregar_producto(request):
    if request.method=='POST':
        form= ProductoForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celular:productos')
        
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
        form = CompraForm()
        
    return render(request,"compras_form.html",{'form': form }) 


def clientes (request):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes 
    }
    return render(request,'clientes.html', context )

def agregar_cliente(request):
    if request.method=='POST':
        form= ClienteForm(request.POST ,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('catalogo_celular:index')
        
    else:   
        form = ClienteForm()
        
    return render(request,"clientes_form.html",{'form': form }) 

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celular:clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes_form.html', {'form': form})

def eliminar_cliente(required, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect('catalogo_celular:clientes')




class CustomLoginView(LoginView):
   template_name="login.html"
       

