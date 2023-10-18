from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    miHtml = open("./ProyectoFinal/plantillas/template.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)