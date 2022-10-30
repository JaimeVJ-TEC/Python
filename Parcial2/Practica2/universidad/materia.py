from django.shortcuts import render,get_object_or_404,redirect
from universidad.models import *
from universidad.forms import *


def detalleMateria(request,id):
    materia = get_object_or_404(Materia, pk=id)
    return render(request,'./Materia/detalleMateria.html',{'materia' :materia})

def agregarMateria(request):
    if request.method =="POST":
        formaMateria = MateriaForm(request.POST)
        if formaMateria.is_valid():
            formaMateria.save()
            return redirect('materia')
    else:
        formaMateria=MateriaForm()
        return render(request,'./Materia/agregarMateria.html',{'formaMateria':formaMateria})

def editarMateria(request,id):
    materia = get_object_or_404(Materia, pk=id)
    if request.method == "POST":
        formaMateria= MateriaForm(request.POST,instance=materia)
        if formaMateria.is_valid():
            formaMateria.save()
            return redirect('materia')
    else:
        formaMateria=MateriaForm(instance=materia)
        return render(request,'./Materia/editarMateria.html',{'formaMateria':formaMateria})

def eliminarMateria(request,id):
    materia = get_object_or_404(Materia, pk=id)
    if (materia):
        materia.delete()
    return redirect('materia')