from django.urls import path
from clinica.views import inicio, crear_paciente, crear_medico
urlpatterns = [
    path('', inicio, name='inicio'),
    path('pacientes/crear/', crear_paciente, name='crear_paciente'),
    path('medicos/crear/', crear_medico, name='crear_medico'),
]