from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from elector import Elector
from candidato import Candidato
from comite_electoral import Comite_electoral

comite1 = Comite_electoral('jose', 123456, 'password')
comite2 = Comite_electoral('pablo', 123457, 'password')

comites=[comite1,comite2] # Lista de comite

candidato1 = Candidato('javier milei',97, 'KML')
candidato2 = Candidato('sergio massa',98, 'XYZ')
candidato3 = Candidato('patricia bullrich',99, 'RQT')
candidatos=[candidato1, candidato2, candidato3]   # lista de candidatos

elector1 = Elector('Mauricio Nestor',9344284, True,'2003-09-20','Apaza','Callapa')
elector2 = Elector('miguel pérez',23, True, '2004-10-10','roble','gueon')
elector3 = Elector('luis cuadros',24, True,'2005-01-21','perez', 'aeaon' )

electores=[elector1, elector2, elector3]   # lista de electores

votos =[]  # lista de votos

app = Flask(__name__, static_url_path='/templates/Style')
app.secret_key = 'cochabamba'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/')
def index():
    return render_template('loginUsuario.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    id_elector = request.form['input-carnet']
    fn_elector_str = request.form['input-fn']
    fn_elector = datetime.strptime(fn_elector_str, '%Y-%m-%d').date()

    registrado = False

    if not id_elector or not fn_elector:
        flash('Por favor, complete ambos campos.', 'error')
        return render_template('loginUsuario.html')

    indice_elector = -1

    for elector in electores:
        ci = str(elector.get_ci())
        nombre = str(elector.get_nombre())  # nombre
        habilitado =  elector.habilitado # habilitado
        apellido1 = elector.apellidoPaterno
        apellido2 = elector.apellidoMaterno
        fechaNacimiento = datetime.strptime(elector.fnacmiento, '%Y-%m-%d').date()

        if ci == id_elector and fechaNacimiento == fn_elector:
            registrado = True
            estado = 'habilitado' if elector.habilitado else 'NO HABILITADO'
            return render_template('perfil.html', nombre=nombre, apellidoPaterno = apellido1, apellidoMaterno = apellido2, ci=id_elector,fechaNacimiento=fn_elector,estado=estado,indice_elector=indice_elector)

    if not registrado:
        flash('CI y/o fecha de nacimiento incorrecta, por favor vuelve a ingresar los datos.', 'error')

    return render_template('loginUsuario.html')

@app.route('/comite')
def index2():
        return render_template('loginComite.html')

@app.route('/verificar_comite', methods=['POST'])
def verificar_comite():
    id_comite = request.form['input-ci']
    pass_comite = request.form['input-contra']

    registrado = False

    if not id_comite or not pass_comite:
        flash('Por favor, complete ambos campos.', 'error')
        return render_template('loginComite.html')

    indice_elector = -1

    for comite in comites:
        ci = str(comite.get_ci())
        contra = str(comite.get_contrasena()) #No estaba llamando al metodo get_contrasena

        if ci == id_comite and contra == pass_comite:
            registrado = True
            return render_template('verResultados.html')

    if not registrado:
        flash('CI y/o Contraseña incorrecta, por favor vuelve a ingresar los datos.', 'error')

    return render_template('loginComite.html')
