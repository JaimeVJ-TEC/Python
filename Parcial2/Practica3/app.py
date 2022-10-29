from flask import Flask, request,jsonify ,url_for, render_template, redirect
from database import db
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
import logging
from flask_migrate import Migrate
from forms import MateriaForm, ProfesorForm
from models import Estudiante
from models import Profesor
from models import Materia

app = Flask(__name__)

#Configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'practica3'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACE_MODIFICATION'] = False

app.config['SECRET_KEY'] = 'algofacil'

logging.basicConfig(filename='error.log',level=logging.DEBUG)

db.init_app(app)

#Configurar migracion
migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/estudiante',methods=["GET","POST"])
def getEstudiantes():
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        estudiantes = Estudiante.query.all()
        return jsonify(estudiantes = Estudiante.serialize_list(estudiantes))
    elif request.method == "POST":
        info = request.json
        estudiante = Estudiante(nombre=info["nombre"], apellido = info["apellido"], email= info["email"], 
                                edad = info["edad"], semestre = info["semestre"], promedio = info["promedio"])
        db.session.add(estudiante)
        db.session.commit()
        return "Estudiante agregado"

@app.route('/estudiante/<int:id>',methods=["GET","PATCH","DELETE"])
def getEstudiante(id):
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        estudiante = Estudiante.query.get_or_404(id)
        return jsonify(Estudiante.serialize(estudiante))
    elif request.method == "PATCH":
        info = request.json
        estudiante = Estudiante.query.get_or_404(id)
        estudiante.nombre = info["nombre"]
        estudiante.apellido = info["apellido"]
        estudiante.email = info["email"]
        estudiante.edad = info["edad"]
        estudiante.semestre = info["semestre"]
        estudiante.promedio = info["promedio"]
        db.session.commit()
        return "Estudiante actualizado"
    elif request.method == "DELETE":
        info = request.json
        estudiante = Estudiante.query.get_or_404(id)
        db.session.delete(estudiante)
        db.session.commit()
        return "Estudiante eliminado"

@app.route('/profesores')
def profesores():
    app.logger.debug(request.headers.get('token'))
    profesores = Profesor.query.all()
    return render_template('/profesor/profesores.html',profesores = profesores)

@app.route('/profesores/<int:id>')
def verProfesor(id):
    app.logger.debug(request.headers.get('token'))
    profesor = Profesor.query.get_or_404(id)
    return render_template('/profesor/detalleProfesor.html',profesor = profesor)

@app.route('/profesores/agregar', methods=["GET","POST"])
def agregarProfesor():
    app.logger.debug(request.headers.get('token'))
    profesor = Profesor()
    profesorForm = ProfesorForm(obj=profesor)
    if request.method == "POST":
        if profesorForm.validate_on_submit():
            profesorForm.populate_obj(profesor)
            db.session.add(profesor)
            db.session.commit()
            return redirect(url_for("profesores"))
    return render_template('/profesor/agregarProfesor.html',forma=profesorForm)

@app.route('/profesores/editar/<int:id>', methods=["GET","POST"])
def editarProfesor(id):
    app.logger.debug(request.headers.get('token'))
    profesor = Profesor.query.get_or_404(id)
    profesorForm = ProfesorForm(obj=profesor)
    if request.method == "POST":
        if profesorForm.validate_on_submit():
            profesorForm.populate_obj(profesor)
            db.session.commit()
            return redirect(url_for("profesores"))
    return render_template('/profesor/editarProfesor.html',forma=profesorForm)

@app.route('/profesores/eliminar/<int:id>')
def eliminarProfesor(id):
    app.logger.debug(request.headers.get('token'))
    profesor = Profesor.query.get_or_404(id)
    db.session.delete(profesor)
    db.session.commit()
    return redirect(url_for('profesores'))

@app.route('/materias')
def materias():
    app.logger.debug(request.headers.get('token'))
    materias = Materia.query.all()
    return render_template('/materia/materias.html',materias = materias)

@app.route('/materias/<int:id>')
def verMateria(id):
    app.logger.debug(request.headers.get('token'))
    materia = Materia.query.get_or_404(id)
    return render_template('/materia/detalleMateria.html',materia = materia)

@app.route('/materias/agregar', methods=["GET","POST"])
def agregarMateria():
    app.logger.debug(request.headers.get('token'))
    materia = Materia()
    materiaForm = MateriaForm(obj=materia)
    materiaForm.profesor_id.choices = [(p.id, p.nombre) for p  in Profesor.query.all()]
    if request.method == "POST":
        if materiaForm.validate_on_submit():
            materiaForm.populate_obj(materia)
            materia.profesor = Profesor.query.get_or_404(materia.profesor_id)
            db.session.add(materia)
            db.session.commit()
            return redirect(url_for("materias"))
    return render_template('/materia/agregarMateria.html', forma = materiaForm)

@app.route('/materias/editar/<int:id>', methods=["GET","POST"])
def editarMateria(id):
    app.logger.debug(request.headers.get('token'))
    materia = Materia.query.get_or_404(id)
    materiaForm = MateriaForm(obj=materia)
    materiaForm.profesor_id.choices = [(p.id, p.nombre) for p  in Profesor.query.all()]
    if request.method == "POST":
        if materiaForm.validate_on_submit():
            materiaForm.populate_obj(materia)
            materia.profesor = Profesor.query.get_or_404(materia.profesor_id)
            db.session.commit()
            return redirect(url_for("materias"))
    return render_template('/materia/editarMateria.html', forma = materiaForm)


@app.route('/materias/eliminar/<int:id>')
def eliminarMateria(id):
    app.logger.debug(request.headers.get('token'))
    materia = Materia.query.get_or_404(id)
    db.session.delete(materia)
    db.session.commit()
    return redirect(url_for('materias'))

@app.errorhandler(404)
def noEncontrado(error):
    return render_template('404.html',error=error),404