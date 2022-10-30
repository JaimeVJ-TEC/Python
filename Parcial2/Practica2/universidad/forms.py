from django.forms import ModelForm,EmailInput,DateInput,CheckboxSelectMultiple
from universidad.models import *
class MateriaForm(ModelForm):
    class Meta:
        model=Materia
        fields= '__all__'
        widgets= {}

class TutorForm(ModelForm):
    class Meta:
        model=Tutor
        fields= '__all__'
        widgets= {
            'correo_electronico': EmailInput(attrs={'type':'email'})
        }

class EstudianteForm(ModelForm):
    class Meta:
        model=Estudiante
        fields= '__all__'
        widgets= {
            'correo_electronico': EmailInput(attrs={'type':'email'})
        }

class ProfesorForm(ModelForm):
    class Meta:
        model=Profesor
        fields= '__all__'
        tup= tuple(Materia.objects.all())
        widgets= {
            'fecha_nacimiento': DateInput(attrs={'type':'date'}),
            'correo_electronico': EmailInput(attrs={'type':'email'}),
            'materias':CheckboxSelectMultiple(choices=tup)
        }