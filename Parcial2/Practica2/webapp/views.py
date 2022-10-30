from django.shortcuts import render
from universidad.models import *
# Create your views here.

def Bienvenida(request):
    return render(request,'index.html')

def VerMateria(request):
    materias = Materia.objects.order_by('id')
    return render(request,'Materia.html',{'materias' : materias})

def VerTutor(request):
    tutores = Tutor.objects.order_by('id')
    return render(request,'Tutor.html',{'tutores' : tutores})

def VerEstudiantes(request):
    estudiantes = Estudiante.objects.order_by('id')
    return render(request,'Estudiante.html',{'estudiantes' : estudiantes})

def VerProfesores(request):
    profesores = Profesor.objects.order_by('id')
    return render(request,'Profesor.html',{'profesores' : profesores})