from django.urls import path
from App import views

urlpatterns = [
    path('/', views.inicio, name= 'Inicio'),
    path('item/', views.item, name= 'Item'),
    path('objeto/', views.objeto, name= 'Objeto'),
    path('usuario/', views.usuario, name= 'Usuario'),
    #path('itemFormulario/', views.formularioItem, name= 'FormularioI'),
    path('formularioUsuario/', views.formUsuario, name='FormularioU'),
    path('buscandoItem/', views.buscarItem, name='BuscarI'),
    path('buscar/', views.buscar),
]
