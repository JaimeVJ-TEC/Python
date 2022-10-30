from django.shortcuts import render,get_object_or_404,redirect
from universidad.models import *
from universidad.forms import *


def detalleEstudiante(request,id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    return render(request,'./Estudiante/detalleEstudiante.html',{'estudiante' :estudiante})

def agregarEstudiante(request):
    if request.method =="POST":
        formaEstudiante = EstudianteForm(request.POST)
        if formaEstudiante.is_valid():
            formaEstudiante.save()
            return redirect('estudiante')
    else:
        formaEstudiante=EstudianteForm()
        return render(request,'./Estudiante/agregarEstudiante.html',{'formaEstudiante':formaEstudiante})

def editarEstudiante(request,id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if request.method == "POST":
        formaEstudiante= EstudianteForm(request.POST,instance=estudiante)
        if formaEstudiante.is_valid():
            formaEstudiante.save()
            return redirect('estudiante')
    else:
        formaEstudiante=EstudianteForm(instance=estudiante)
        return render(request,'./Estudiante/editarEstudiante.html',{'formaEstudiante':formaEstudiante})

def eliminarEstudiante(request,id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if (estudiante):
        estudiante.delete()
    return redirect('estudiante')