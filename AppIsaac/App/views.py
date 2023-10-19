from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def item(request):
    return HttpResponse("Vista items")

def objeto(request):
    return HttpResponse("Vista objetos")

def usuario(request):
    return HttpResponse("Vista usuario")

