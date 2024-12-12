from django.shortcuts import render,redirect
from .forms import *

def index(request):
    return render(request, "index.html")

def crear(request):
    if request.method == 'POST': 
        formulario = FormularioForm(request.POST)  
        
        if formulario.is_valid():  
            formulario.save()  
            redirect ('crear_exitoso')
    else:
        formulario = FormularioForm()  
        
    return render(request, 'Formularios/crear.html', {'formulario': formulario})

        
        
        