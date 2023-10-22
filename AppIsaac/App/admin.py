from django.contrib import admin
from .models import Item, Objeto, Usuario

admin.site.register(Item)
admin.site.register(Objeto)
admin.site.register(Usuario)

def __str__(self):
    return f"Nombre: {self.nombre} - Personaje: {self.personaje} - Mail: {self.email}"