from serializer import Serializer
from app import db

class Profesor(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    edad = db.Column(db.Integer)
    materias = db.relationship('Materia',backref='profesor')

    def __repr__(self):
        return (f'{self.nombre} {self.apellido}, ID:{self.id}')

    
class Estudiante(db.Model,Serializer):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
    edad = db.Column(db.Integer)
    semestre = db.Column(db.Integer)
    promedio = db.Column(db.Float)

    def __str__(self) -> str:
        return (f'ID: {self.id}',
                f'Nombre: {self.nombre} {self.apellido}', 
                f'Email: {self.email}',
                f'Edad: {self.edad}',
                f'Semestre: {self.semestre}',
                f'Promedio: {self.promedio}')

class Materia(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    creditos = db.Column(db.Integer)
    horas = db.Column(db.Integer)
    semestre = db.Column(db.Integer)
    profesor_id = db.Column(db.Integer,db.ForeignKey('profesor.id'),nullable=False)

    def __str__(self) -> str:
        return (f'ID: {self.id}',
                f'Nombre: {self.nombre}', 
                f'Creditos: {self.creditos}',
                f'Horas: {self.horas}',
                f'Semestre: {self.semestre}',
                f'Profesor: {self.profesor}')