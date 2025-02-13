from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gemalopez:Wt2Yo461rS15tzRqQas4krG49EP9pJ9t@dpg-cuiikijqf0us73dpub7g-a.oregon-postgres.render.com/db_cetech_g3j3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de la base de datos
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

    def to_dict(self):
        return{
            'no_control': self.no_control,
            'nombre': self.nombre,
            'ap_paterno': self.ap_paterno,
            'ap_materno': self.ap_materno,
            'semestre': self.semestre,
        }

#Ruta raiz
@app.route('/')
def index():
    #Trae todos los alumnos
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos = alumnos)

#Ruta /alumnos
@app.route('/alumnos/new', methods=['POST', 'GET'])
def create_alumno():
    if request.method == 'POST':
        #Agregar un nuevo alumno
        no_control = request.form['no_control']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        semestre = request.form['semestre']

        nvo_alumno = Alumno(no_control=no_control, nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, semestre=semestre)
        db.session.add(nvo_alumno)
        db.session.commit()
        return redirect(url_for('index'))
    #Si no es POST, regresa el formulario
    return render_template('create_alumno.html')


if __name__ == '__main__':
    app.run(debug=True)