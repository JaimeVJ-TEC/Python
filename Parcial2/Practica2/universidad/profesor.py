from django.shortcuts import render,get_object_or_404,redirect
from universidad.models import *
from universidad.forms import *

def detalleProfesor(request,id):
    profesor = get_object_or_404(Profesor, pk=id)
    return render(request,'./Profesor/detalleProfesor.html',{'profesor' :profesor})

def agregarProfesor(request):
    if request.method =="POST":
        formaProfesor = ProfesorForm(request.POST)
        if formaProfesor.is_valid():
            formaProfesor.save()
            return redirect('profesor')
    else:
        formaProfesor=ProfesorForm()
        return render(request,'./Profesor/agregarProfesor.html',{'formaProfesor':formaProfesor})

def editarProfesor(request,id):
    profesor = get_object_or_404(Profesor, pk=id)
    if request.method == "POST":
        formaProfesor= ProfesorForm(request.POST,instance=profesor)
        if formaProfesor.is_valid():
            formaProfesor.save()
            return redirect('profesor')
    else:
        formaProfesor=ProfesorForm(instance=profesor)
        return render(request,'./Profesor/editarProfesor.html',{'formaProfesor':formaProfesor})

def eliminarProfesor(request,id):
    profesor = get_object_or_404(Profesor, pk=id)
    if (profesor):
        profesor.delete()
    return redirect('profesor')