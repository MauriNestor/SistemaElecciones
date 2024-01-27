from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class Persona:
    def __init__(self, nombre, ci):
        self.__nombre = nombre.title()
        self.__ci = ci

    def get_nombre(self):
        return self.__nombre

    def get_ci(self):
        return self.__ci

class Candidato(Persona):
    def __init__(self, nombre, ci, partido):
        super().__init__(nombre, ci)
        self.__partido = partido
        self.__image_path = partido + '.jpg'

    @property
    def partido(self):
        return self.__partido

    @property
    def image_path(self):
        return self.__image_path

class Elector(Persona):
    def __init__(self, nombre, ci, habilitado,fechaNacimiento ):
        super().__init__(nombre, ci)
        self.__fechaNacimiento = fechaNacimiento
        self.__habilitado = habilitado

    @property
    def habilitado(self):
        return self.__habilitado
    @property
    def fnacmiento(self):
        return self.__fechaNacimiento

    @habilitado.setter
    def habilitado(self, habilitado):
        self.__habilitado = habilitado

class Voto:
    def __init__(self, elector, voto):
        self.__elector = elector
        self.__voto = voto

    @property
    def voto(self):
        return self.__voto

    def emitir_voto(self):
        if self.__elector.habilitado:
            self.__elector.habilitado = False
        else:
            print('Usted {} ya realizó su voto ... estado habilitación:{}'.format(self.__elector.get_nombre(), False ))

candidato1 = Candidato('javier milei',97, 'KML')
candidato2 = Candidato('sergio massa',98, 'XYZ')
candidato3 = Candidato('patricia bullrich',99, 'RQT')
candidatos=[candidato1, candidato2, candidato3]   # lista de candidatos

elector1 = Elector('Mauricio Apaza',9344284, True,'2003-09-20')
elector2 = Elector('miguel pérez',23, True, '2004-10-10')
elector3 = Elector('luis cuadros',24, True,'2005-01-21' )

electores=[elector1, elector2, elector3]   # lista de electores

votos =[]  # lista de votos

app = Flask(__name__, static_url_path='/templates/Style/login.css')
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
        fechaNacimiento = datetime.strptime(elector.fnacmiento, '%Y-%m-%d').date()

        if ci == id_elector and fechaNacimiento == fn_elector:
            registrado = True
            estado = 'habilitado' if elector.habilitado else 'NO HABILITADO'
            return render_template('perfil.html', nombre=nombre, ci=id_elector,fechaNacimiento=fn_elector,estado=estado,indice_elector=indice_elector)

    if not registrado:
        flash('CI y/o fecha de nacimiento incorrecta, por favor vuelve a ingresar los datos.', 'error')

    return render_template('loginUsuario.html')

