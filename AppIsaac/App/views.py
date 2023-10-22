from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from App.models import *    
from App.forms import *

def inicio(request):
    return render(request, "App/inicio.html")

#def item(request):
#    return render(request, "App/item.html")

def objeto(request):
    return render(request, "App/objeto.html")

#def usuario(request):
#   return render(request, "App/usuario.html")

def item(request):
    if request.method == "POST":
        miForm = FormularioItem(request.POST)
        print(miForm)
        
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            
            item = Item(request.POST['nombre'], request.POST['precio'])
            item.save()
        
            return render(request, "App/inicio.html")
    else:
        miForm = FormularioItem()
     
    return render(request, "App/item.html", {"miForm": miForm})

def usuario(request):
    if request.method == "POST":
        miForm = FormUsuario(request.POST)
        print(miForm)
        
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            
            usuario = Usuario(nombre=informacion['nombre'], personaje=informacion['personaje'],
            email=informacion['email'])
            usuario.save()
            
            return render(request, "App/inicio.html")
    else:
        miForm = FormUsuario()
        
    return render(request, "App/usuario.html", {"miForm": miForm})
             
def formUsuario(request):
    if request.method == "POST":
        miForm = FormUsuario(request.POST)
        print(miForm)
        
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            
            usuario = Usuario(request, nombre=informacion['nombre'], personaje=informacion['personaje'],
                email=informacion['email'])
            usuario.save()
            
            return render(request, "App/inicio.html")
    else:
        miForm = FormUsuario()
        
    return render(request, "App/formularioU.html", {"miForm": miForm})

def buscarItem(request):
    return render(request, "App/buscarI.html")

def buscar(request):
    
    if request.GET["precio"]:
        precio = request.GET['precio']
        item = item.objects.filter(precio_icontains=precio)
        
        return render(request, "App/resultadoBusqueda.html", {"nombre":item, "precio":precio})
    
    else:
        respuesta = "No hay datos"
    
    return render(request, "App/inicio.html", {"respuesta":respuesta})

def leerUsuarios(request):
    usuario = Usuario.objects.all()
    contexto = {"usuario": usuario}
    return render(request, "App/leerUsuario.html", contexto)

def eliminarUsuario(request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    usuario.delete()
    
    usuario = Usuario.objects.all()
    
    contexto = {"usuario": usuario}
    
    return render(request, "App/leerUsuario.html", contexto)

def editarUsuario(request, usuario_nombre):
    usuario = Usuario.objects.get(usuario_nombre)
    
    if request.method == 'POST':
        
        miForm = FormUsuario(request.POST)
        print(miForm)
        
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            
            usuario.nombre = informacion['nombre']
            usuario.personaje = informacion['personaje']
            usuario.email = informacion['email']
            
            usuario.save()
            return render(request, "App/inicio.html")
        
    else:
        miForm = FormUsuario(initial={'nombre': usuario.nombre, 'personaje': usuario.personaje,
        'email': usuario.email})
    
    return render(request, "App/editarUsuario.html", {"miForm": miForm, "usuario_nombre": usuario_nombre})

#########################################################

class ItemList(ListView):
    model = Item
    template_name = "App/i_list.html"
    
class ItemDetalle(DetailView):
    model = Item
    template_name = "App/i_detalle.html"

class ItemCreacion(CreateView):
    model = Item
    success_url = "App/item/list"
    fields = ['nombre', 'precio']
    
class ItemUpdate(UpdateView):
    model = Item
    success_url = "App/item/list"
    fields = ['nombre', 'precio']
    
class ItemDelete(DeleteView):
    model = Item
    success_url = "App/item/list"