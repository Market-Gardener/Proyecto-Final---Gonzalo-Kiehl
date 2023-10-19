from django.http import HttpResponse
from django.template import Template, Context, loader
from App.models import Item

def saludo(request):
    nombre = "Jose"
    apellido = "Perez"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [7, 4, 8, 3]}
    
    miHtml = open('./AppIsaac/Plantillas/template1.html')
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    contexto = Context()
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def usando_loader(request):
    diccionario ={
        "nombre": nombre,
        "apellido": apellido,
        "notas": [7, 4, 8, 3],
    }
    
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def llave(request, nombre, numero):
    llave = Item(nombre = nombre, precio= int(numero))
    llave.save()
    documento =f"Item: {llave.nombre}<br>Precio: ${llave.precio}"
    return HttpResponse(documento)