from django.db import models

class Tutor(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'

class Estudiante(models.Model):
    numero_control = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    semestre = models.CharField(max_length=255)
    tutor = models.OneToOneField(Tutor,on_delete=models.CASCADE,primary_key=False)

    def __str__(self) -> str:
        return f'{self.id} Estudiante {self.numero_control}: {self.nombre} {self.apellidos}'

class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    semestre = models.CharField(max_length=255)
    creditos_teoricos = models.IntegerField()
    creditos_practicos = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.id}.- {self.nombre}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento= models.DateField(auto_now=False)
    correo_electronico = models.CharField(max_length=255)
    numero_seguro = models.CharField(max_length=255)
    telefono=models.CharField(max_length=255)
    materias = models.ManyToManyField(Materia)

    def __str__(self) -> str:
        return f'{self.id}.- {self.nombre}'