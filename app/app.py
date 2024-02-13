from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = 'cochabamba'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{clave}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'MauriApaza845',
        clave = 'Mauricio67532900.',
        servidor = 'MauriApaza845.mysql.pythonanywhere-services.com',
        database = 'MauriApaza845$sistemaEleccionesDB'
    )
db = SQLAlchemy(app)

class Elector(db.Model):
    ci_elector = db.Column(db.String(8), primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido_paterno = db.Column(db.String(80), nullable=False)
    apellido_materno = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name


class Candidato(db.Model):
    id_candidato = db.Column(db.String(8), primary_key=True)
    nombre_candidato = db.Column(db.String(50), nullable=False)
    nombre_partido = db.Column(db.String(20), nullable=False)
    foto_candidato = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name
    def contar_votos(self):
        return db.session.query(func.count(Voto.id_voto)).filter_by(id_candidato=self.id_candidato).scalar()

class Voto(db.Model):
    id_voto = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ci_elector = db.Column(db.String(8), db.ForeignKey('elector.ci_elector'), nullable=False)
    id_candidato = db.Column(db.String(8), db.ForeignKey('candidato.id_candidato'), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name

class Comite(db.Model):
    __tablename__ = 'comite_electoral'
    id_comite = db.Column(db.Integer,primary_key = True,nullable=False)
    ci_comite = db.Column(db.String(10),nullable=False)
    contrasena = db.Column(db.String(25),nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')
def index():
    return render_template('loginUsuario.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    ci_carnet = request.form.get('input-carnet')
    fecha_nacimiento = request.form.get('input-fn')

    if not ci_carnet or not fecha_nacimiento:
        flash('Por favor, completa ambos campos.', 'error')
        return render_template('loginUsuario.html')

    elector = Elector.query.filter_by(ci_elector=ci_carnet).first()

    if elector:
        pass_elec = elector.fecha_nacimiento.strftime('%Y-%m-%d')
        if fecha_nacimiento == pass_elec:
            fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
            edad = (datetime.now() - fecha_nacimiento_dt).days // 365
            if edad < 18:
                flash('Solo pueden votar personas mayores a 18 años.', 'error')
                return render_template('loginUsuario.html')

            session['elector_logueado'] = elector.ci_elector

            return render_template('perfil.html', elector = elector)
        else:
            flash('CI y/o fecha de nacimiento incorrecta, por favor vuelve a ingresar los datos.', 'error')
            return render_template('loginUsuario.html')
    else:
        flash('CI y/o fecha de nacimiento incorrecta, por favor vuelve a ingresar los datos.', 'error')
        return render_template('loginUsuario.html')


@app.route('/comite')
def index2():
        return render_template('loginComite.html')

@app.route('/verificar_comite', methods=['POST'])
def verificar_comite():
    ci_comite = request.form.get('input-ci')
    contrasena = request.form.get('input-contra')

    if not ci_comite or not contrasena:
        flash('Por favor, completa ambos campos.', 'error')
        return render_template('loginComite.html')

    comite = Comite.query.filter_by(ci_comite=ci_comite).first()

    if comite:
        if contrasena == comite.contrasena:
            session['comite_logueado'] = comite.ci_comite
            flash('Bienvenido')
            candidatos = Candidato.query.all()
            cantidadtotal = Voto.query.count()
            cantidadelectores = Elector.query.count()
            return render_template('verResultados.html', candidatos=candidatos, cantidadtotal = cantidadtotal, cantidadelectores = cantidadelectores)
        else:
            flash('CI y/o contraseña incorrecta, por favor vuelve a ingresar los datos.', 'error')
            return render_template('loginComite.html')
    else:
        flash('CI y/o contraseña incorrecta, por favor vuelve a ingresar los datos.', 'error')
        return render_template('loginComite.html')



@app.route('/irVotar', methods=['POST'])
def irVotar():

    candidatos = Candidato.query.all()
    return render_template('votar.html', candidatos=candidatos)


@app.route('/realizar_votacion', methods=['POST'])
def realizar_votacion():
    ci_elector = session.get('elector_logueado')
    elector_logeado = Elector.query.get(ci_elector)
    candidatos = Candidato.query.all()

    if elector_logeado:
        id_candidato = request.form.get('candidato_ci')
        if id_candidato:
            voto = Voto(ci_elector=ci_elector, id_candidato=id_candidato)
            db.session.add(voto)
            elector_logeado.estado = 'desahibilitado'
            db.session.commit()
            flash('Votación realizada con éxito.')
            return render_template('loginUsuario.html')
        else:
            flash('Por favor, selecciona un candidato antes de votar.', 'error')
            return render_template('votar.html', candidatos=candidatos)
    return render_template('votar.html', candidatos=candidatos)


