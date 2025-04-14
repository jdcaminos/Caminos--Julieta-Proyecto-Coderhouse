from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionPaciente, CreacionMedico
from home.models import Paciente, Medico

# Create your views here.
def inicio(request):
    return render(request, 'home/inicio.html')

def crear_paciente(request):

    print('Estos son los datos del GET', request.GET)
    print('Estos son los datos del GET', request.POST)

    if request.method == "POST":
        formulario = CreacionPaciente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            paciente = Paciente(nombre=info.get('nombre'), apellido=info.get('apellido'))
            paciente.save()
            return redirect('inicio')
    else:
        formulario = CreacionPaciente()

    return render(request, 'home/crear_paciente.html', {'formulario': formulario}) 

def crear_medico(request):

    print('Estos son los datos del GET', request.GET)
    print('Estos son los datos del GET', request.POST)

    if request.method == "POST":
        formulario = CreacionMedico(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            medico = Medico(nombre=info.get('nombre'), apellido=info.get('apellido'))
            medico.save()
            return redirect('inicio')
    else:
        formulario = CreacionMedico()

    return render(request, 'home/crear_medico.html', {'formulario': formulario})   
