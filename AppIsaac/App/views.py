from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

def inicio(request):
    return render(request, "App/padre.html")

def item(request):
    return HttpResponse("Vista items")

def objeto(request):
    return HttpResponse("Vista objetos")

def usuario(request):
    return HttpResponse("Vista usuario")
