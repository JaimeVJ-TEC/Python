"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *
from universidad.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Bienvenida,name='index'),
    path('Materia',VerMateria,name='materia'),
    path('Tutor',VerTutor,name='tutor'),
    path('Estudiante',VerEstudiantes,name='estudiante'),
    path('Profesor',VerProfesores,name='profesor'),

    path('detalleMateria/<int:id>',detalleMateria),
    path('agregarMateria',agregarMateria),
    path('editarMateria/<int:id>',editarMateria),
    path('eliminarMateria/<int:id>',eliminarMateria),

    path('detalleTutor/<int:id>',detalleTutor),
    path('agregarTutor',agregarTutor),
    path('editarTutor/<int:id>',editarTutor),
    path('eliminarTutor/<int:id>',eliminarTutor),

    path('detalleEstudiante/<int:id>',detalleEstudiante),
    path('agregarEstudiante',agregarEstudiante),
    path('editarEstudiante/<int:id>',editarEstudiante),
    path('eliminarEstudiante/<int:id>',eliminarEstudiante),

    path('detalleProfesor/<int:id>',detalleProfesor),
    path('agregarProfesor',agregarProfesor),
    path('editarProfesor/<int:id>',editarProfesor),
    path('eliminarProfesor/<int:id>',eliminarProfesor)

]
