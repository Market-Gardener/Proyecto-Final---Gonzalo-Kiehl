from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    miHtml = open('./AppIsaac/Plantillas/template1.html')
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    contexto = Context()
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)