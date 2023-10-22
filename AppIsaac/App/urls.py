from django.urls import path
from App import views

urlpatterns = [
    path('/', views.inicio, name= 'Inicio'),
    path('item/', views.item, name= 'Item'),
    path('objeto/', views.objeto, name= 'Objeto'),
    path('usuario/', views.usuario, name= 'Usuario'),
    #path('itemFormulario/', views.formularioItem, name= 'FormularioI'),
    #path('formularioUsuario/', views.formUsuario, name='FormularioU'),
    #path('buscandoItem/', views.buscarItem, name='BuscarI'),
    path('buscar/', views.buscar),
    path('leerUsuario/', views.leerUsuarios, name= 'LeerUsuario'),
    path('eliminarUsuario/<usuario_nombre>/', views.eliminarUsuario, name= 'EliminarUsuartio'),
    path('editarUsuario/<usuario_nombrte>/', views.editarUsuario, name= 'EditarUsuario'),
]

urlpatterns +=[
    path('item/lista/', views.ItemList, name="List"),
    path('item/detalle/<int:pk>/', views.ItemDetalle, name="Detail"),
    path('item/nuevo/', views.ItemCreacion, name='New'),
    path('item/editar/<int:pk>/', views.ItemUpdate, name='Edit'),
    path('item/eliminar/<int:pk>', views.ItemDelete, name='Delete'),
]
