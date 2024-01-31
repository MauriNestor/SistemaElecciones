from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from collections import defaultdict

from elector import Elector
from candidato import Candidato
from comite_electoral import Comite_electoral
from voto import Voto

comite1 = Comite_electoral('jose', 123456, 'password')
comite2 = Comite_electoral('pablo', 123457, 'password')

comites=[comite1,comite2] # Lista de comite
candidatos = []
candidato1 = Candidato('javier milei',97, 'KML','images/baner.jpg')
candidato2 = Candidato('sergio massa',98, 'XYZ','images/yoo.JPG')
candidato3 = Candidato('patricia bullrich',99, 'RQT','images/yoo.JPG')
candidatos=[candidato1, candidato2, candidato3]   # lista de candidatos

elector1 = Elector('Mauricio Nestor',1,'no habilitado','2003-09-20','Apaza','Callapa')
elector2 = Elector('Miguel Grover',2, 'habilitado', '2003-09-20','Mita','gueon')
elector3 = Elector('luis cuadros',3, 'habilitado','2003-09-20','perez', 'aeaon' )

electores=[elector1, elector2, elector3]   # lista de electores

votos =[]  # lista de votos

app = Flask(__name__, static_url_path='/templates/static/Style')
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

    if not id_elector or not fn_elector_str:
        flash('Por favor, complete ambos campos.', 'error')
        return render_template('loginUsuario.html')

    fn_elector = datetime.strptime(fn_elector_str, '%Y-%m-%d').date()

    indice_elector = -1

    for elector in electores:
        ci = str(elector.get_ci())
        nombre = str(elector.get_nombre())  # nombre
        habilitado =  elector.habilitado # habilitado
        apellido1 = elector.apellidoPaterno
        apellido2 = elector.apellidoMaterno
        fechaNacimiento = datetime.strptime(elector.fnacmiento, '%Y-%m-%d').date()

        if ci == id_elector and fechaNacimiento == fn_elector:
            return render_template('perfil.html', nombre=nombre, apellidoPaterno = apellido1, apellidoMaterno = apellido2, ci=id_elector,fechaNacimiento=fn_elector,habilitado=habilitado,indice_elector=indice_elector)

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
        contra = str(comite.get_contrasena)

        if ci == id_comite and contra == pass_comite:
            registrado = True
            return render_template('verResultados.html')

    if not registrado:
        flash('CI y/o Contraseña incorrecta, por favor vuelve a ingresar los datos.', 'error')

    return render_template('loginComite.html')

@app.route('/irVotar', methods=['POST'])
def irVotar():
    return render_template('votar.html', candidatos=candidatos)



@app.route('/realizar_votacion', methods=['POST'])
def realizar_votacion():
    candidato_ci = request.form.get('candidato_ci')

    for candidato in candidatos:
        if str(candidato.get_ci()) == candidato_ci:
            candidato.aumentar_votos()
            flash('¡Tu voto ha sido registrado!', 'success')
            return render_template('verResultados.html', candidatos=candidatos)

    return render_template('error.html', message='Candidato no encontrado')


#     # Si el candidato seleccionado no se encuentra en la lista, mostrar un mensaje de error
#     flash('El candidato seleccionado no es válido.', 'error')
#     return redirect(url_for('irVotar'))

# @app.route('/realizar_votacion', methods=['POST'])
# def realizar_votacion():
#     if 'usuario' not in session:
#         flash('Por favor, inicia sesión para votar.', 'error')
#         return redirect(url_for('index'))

#     candidato_id = int(request.form['candidato_id'])

#     # Encuentra el elector que está votando
#     elector_votante = next((e for e in electores if e.get_ci() == session['usuario']), None)

#     # Encuentra el candidato seleccionado
#     candidato_seleccionado = next((c for c in candidatos if c.id == candidato_id), None)

#     if elector_votante and candidato_seleccionado:
#         # Verifica que el elector no haya votado previamente
#         if not any(v.elector.get_ci() == elector_votante.get_ci() for v in votos):
#             # Crea un objeto Voto y guárdalo en la lista de votos
#             voto = Voto(elector_votante, candidato_seleccionado)
#             votos.append(voto)
#             flash('¡Tu voto ha sido registrado!', 'success')
#         else:
#             flash('Ya has votado previamente. No se permiten votos duplicados.', 'error')
#     else:
#         flash('Hubo un problema al procesar tu voto. Por favor, inténtalo nuevamente.', 'error')

#     return redirect(url_for('index'))

# voto1 = Voto(candidato1)
# voto2 = Voto(candidato1)
# voto3 = Voto(candidato2)
# voto4 = Voto(candidato3)
# voto5 = Voto(candidato1)
# voto6 = Voto(candidato2)

# votos =[voto1,voto2,voto3,voto4,voto5, voto6]  # lista de votos

# @app.route('/ver_resultado', methods=['GET'])
# def ver_res():
#     resultados = calcular_resultados()
#     return render_template('verResultados.html',resultados=resultados)


# def calcular_resultados():
#     resultados = {}
#     for voto in votos:
#         candidato = voto.get_candidato.get_nombre()  # Acceder al atributo sin paréntesis
#         partido = voto.get_candidato.get_partido
#         if candidato not in resultados:
#             resultados[candidato,partido] = 0
#         resultados[candidato,partido] += 1
#     return resultados