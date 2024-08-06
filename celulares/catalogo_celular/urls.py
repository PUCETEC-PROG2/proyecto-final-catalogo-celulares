from django.urls import path
from . import views


app_name= 'catalogo_celular'

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    # path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    # path("login/", views.CustomLoginView.as_view(), name="login"),
]

