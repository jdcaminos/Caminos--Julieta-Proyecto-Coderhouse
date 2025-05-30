from django import forms
from clinica.models import Medico
class CreacionPaciente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
"""
class CreacionMedico(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
"""



class CreacionMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'imagen']
