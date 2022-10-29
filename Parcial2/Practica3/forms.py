from flask import Flask
from models import Profesor,Materia
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class ProfesorForm(FlaskForm):
    nombre = StringField("Nombre: ",validators=[DataRequired()])
    apellido = StringField("Apellido: ",validators=[DataRequired()])
    email = StringField("Email: ")
    edad = IntegerField("Edad: ",validators=[DataRequired()])
    enviar = SubmitField("Aceptar")

class MateriaForm(FlaskForm):
    nombre = StringField("Nombre: ",validators=[DataRequired()])
    creditos = IntegerField("Creditos: ",validators=[DataRequired()])
    horas = IntegerField("Horas: ",validators=[DataRequired()])
    semestre = IntegerField("Semestre: ")
    profesor_id =  SelectField("Profesor: ", coerce=int)
    enviar = SubmitField("Aceptar")