from django.shortcuts import render,get_object_or_404,redirect
from universidad.models import *
from universidad.forms import *

def detalleTutor(request,id):
    tutor = get_object_or_404(Tutor, pk=id)
    return render(request,'./Tutor/detalleTutor.html',{'tutor' :tutor})

def agregarTutor(request):
    if request.method =="POST":
        formaTutor = TutorForm(request.POST)
        if formaTutor.is_valid():
            formaTutor.save()
            return redirect('tutor')
    else:
        formaTutor=TutorForm()
        return render(request,'./Tutor/agregarTutor.html',{'formaTutor':formaTutor})

def editarTutor(request,id):
    tutor = get_object_or_404(Tutor, pk=id)
    if request.method == "POST":
        formaTutor= TutorForm(request.POST,instance=tutor)
        if formaTutor.is_valid():
            formaTutor.save()
            return redirect('tutor')
    else:
        formaTutor=TutorForm(instance=tutor)
        return render(request,'./Tutor/editarTutor.html',{'formaTutor':formaTutor})

def eliminarTutor(request,id):
    tutor = get_object_or_404(Tutor, pk=id)
    if (tutor):
        tutor.delete()
    return redirect('tutor')