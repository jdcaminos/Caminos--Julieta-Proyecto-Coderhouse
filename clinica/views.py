from django.shortcuts import render, redirect
from django.http import HttpResponse
from clinica.forms import CreacionPaciente, CreacionMedico
from clinica.models import Paciente, Medico
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'clinica/inicio.html')

@login_required
def crear_paciente(request):

    print('Estos son los datos del GET', request.GET)
    print('Estos son los datos del GET', request.POST)

    if request.method == "POST":
        formulario = CreacionPaciente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            paciente = Paciente(nombre=info.get('nombre'), apellido=info.get('apellido'), fecha_nacimiento=info.get('fecha_nacimiento'))
            paciente.save()
            return redirect('inicio')
    else:
        formulario = CreacionPaciente()

    return render(request, 'clinica/crear_paciente.html', {'formulario': formulario}) 

@login_required
def crear_medico(request):

    print('Estos son los datos del GET', request.GET)
    print('Estos son los datos del POST', request.POST)

    if request.method == "POST":
        formulario = CreacionMedico(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            medico = Medico(nombre=info.get('nombre'), apellido=info.get('apellido'))
            medico.save()
            return redirect('listado_de_medicos')
    else:
        formulario = CreacionMedico()

    return render(request, 'clinica/crear_medico.html', {'formulario': formulario})   

def listado_de_medicos(request):
    medicos = Medico.objects.all()
    return render (request, 'clinica/listado_de_medicos.html', {'medicos': medicos})

def detalle_medico(request, medico_en_especifico):
    medico = Medico.objects.get(id=medico_en_especifico)
    return render(request, 'clinica/detalle_medico.html', {'medico': medicos})

class VistaDetalleMedico(DetailView):
    model = Medico
    template_name = "clinica/detalle_medico.html"

class VistaModificarMedico(LoginRequiredMixin, UpdateView):
    model = Medico
    template_name = "clinica/modificar_medico.html"
    fields = ["nombre", "apellido", "imagen"]
    success_url = reverse_lazy('listado_de_medicos')

class VistaEliminarMedico(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = "clinica/eliminar_medico.html"
    success_url = reverse_lazy('listado_de_medicos')

