from django import forms

class FormularioItem(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    
class FormUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    personaje = forms.CharField(max_length=30)
    email = forms.EmailField()
    
