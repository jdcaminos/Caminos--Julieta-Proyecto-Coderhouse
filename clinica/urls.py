from django.urls import path, include
from clinica.views import inicio, crear_paciente, crear_medico, detalle_medico, listado_de_medicos, VistaDetalleMedico, VistaModificarMedico, VistaEliminarMedico
from django. contrib import admin
urlpatterns = [
   
    path('', inicio, name='inicio'),
    path('pacientes/crear/', crear_paciente, name='crear_paciente'),
    path('medicos/crear/', crear_medico, name='crear_medico'),
    path('medicos/', listado_de_medicos, name='listado_de_medicos'),
    path('medicos/<int:pk>/eliminar/', VistaEliminarMedico.as_view(), name='eliminar_medico'),
    path('medicos/<int:pk>/', VistaDetalleMedico.as_view(), name='detalle_medico'),
    path('medicos/<int:pk>/modificar/', VistaModificarMedico.as_view(), name='modificar_medico'),
    
]
