from django.shortcuts import render
from .models import Medico, Paciente
from .formularios import add_medic as fm
from.formularios import add_paciente as fm2
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")


def list_med(request):
    medicos = Medico.objects.all()
    return render(request, "listmed.html", {"lismed":medicos})


def list_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "listpacientes.html", {"lispacientes":pacientes})


def add_med(request):
    if request.method == "POST":
        formulario = fm.add_medic(request.POST)
        if formulario.is_valid():
            nuevoreg = Medico()
            nuevoreg.nombre = formulario.data["nombre"]
            nuevoreg.apellido = formulario.data["apellido"]
            nuevoreg.especialidad = formulario.data["especialidad"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.add_medic()
        return render(request, "add_medic.html",{"form":formulario})
    

def add_pac(request):
    if request.method == "POST":
        formulario = fm2.add_paciente(request.POST)
        if formulario.is_valid():
            nuevoregpac = Paciente()
            nuevoregpac.nombre = formulario.data["nombre"]
            nuevoregpac.apellido = formulario.data["apellido"]
            nuevoregpac.fecha_nacimiento = formulario.data["fecha_nacimiento"]
            nuevoregpac.sexo = formulario.data["sexo"]
            nuevoregpac.altura = formulario.data["altura"]
            nuevoregpac.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm2.add_paciente()
        return render(request, "add_paciente.html", {"form":formulario})
    


