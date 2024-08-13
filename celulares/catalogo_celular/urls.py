from django.urls import path
from . import views


app_name= 'catalogo_celular'

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    path('productos/detalle_producto/<int:id>/', views.detalle_producto, name="detalle_producto"),
    path('views_productos/', views.views_productos, name="views_productos"),
    path("agregar_producto/", views.agregar_producto, name="agregar_producto"),
    path("productos/editar_producto/<int:id>/", views.editar_producto, name="editar_producto"),
    path("productos/eliminar_producto/<int:id>/", views.eliminar_producto, name="eliminar_producto"),

    path("compras/", views.compras, name="compras"),
    path("agregar_compra/", views.agregar_compra, name="agregar_compra"),

    path("clientes/", views.clientes, name="clientes"),
    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path("clientes/editar_cliente/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("clientes/eliminar_cliente/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),

    # path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]

