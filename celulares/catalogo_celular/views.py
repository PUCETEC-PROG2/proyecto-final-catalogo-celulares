
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
 
# def pokemon(request, pokemon_id):
#     #SELECT * FROM pokedex_pokemon WHERE id='pokemon_id'
#     pokemon = Pokemon.objects.get(id=pokemon_id)
#     template = loader.get_template('display_pokemon.html')
#     context = {
#         'pokemon': pokemon
#     }
#     return HttpResponse(template.render(context, request))

# @login_required    
# def add_pokemon(request):
#     if request.method=='POST':
#         form= PokemonFor(request.POST ,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('pokedex:index')
        
#     else:
    
#         form = PokemonFor()
        
#     return render(request,"add_pokemon.html",{'form': form }) 

#class CustomLoginView(LoginView):
#    template_name="login.html"
       

