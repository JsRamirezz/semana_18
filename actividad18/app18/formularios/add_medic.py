from django import forms

class add_medic(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)

