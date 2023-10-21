from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from App.models import *
from App.forms import *

def inicio(request):
    return render(request, "App/inicio.html")

#def item(request):
#    return render(request, "App/item.html")

def objeto(request):
    return render(request, "App/objeto.html")

def usuario(request):
    return render(request, "App/usuario.html")

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