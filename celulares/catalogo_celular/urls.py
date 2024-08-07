from django.urls import path
from . import views


app_name= 'catalogo_celular'

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    path("productos/editar_producto/<int:id>/", views.editar_producto, name="editar_producto"),
    path("productos/eliminar_producto/<int:id>/", views.eliminar_producto, name="eliminar_producto"),

    path("compras/", views.compras, name="compras"),

    # path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    # path("login/", views.CustomLoginView.as_view(), name="login"),
]

