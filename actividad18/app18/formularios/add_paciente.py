from django import forms

class add_paciente(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateTimeField
    sexo = forms.CharField(max_length=100)
    altura = forms.FloatField()