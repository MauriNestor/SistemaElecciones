import mysql.connector
from mysql.connector import errorcode
from flask_sqlalchemy import SQLAlchemy

print("Conectando...")
try:
    conn = mysql.connector.connect(
           host='MauriApaza845.mysql.pythonanywhere-services.com',
           user='MauriApaza845',
           password='Mauricio67532900.'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe un error en el nombre de usuario o en la clave')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `MauriApaza845$sistemaEleccionesDB`;")

cursor.execute("CREATE DATABASE `MauriApaza845$sistemaEleccionesDB`;")

cursor.execute("USE `MauriApaza845$sistemaEleccionesDB`;")

# creando las tablas
TABLES = {}

TABLES['Administrador'] = ('''
      CREATE TABLE `administrador` (
      `id_admin` int NOT NULL,
      `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `contrasena` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      PRIMARY KEY (`id_admin`) USING BTREE
      ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;''')

TABLES['Candidato'] = ('''
      CREATE TABLE `candidato`  (
      `id_candidato` int NOT NULL AUTO_INCREMENT,
      `nombre_partido` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `nombre_candidato` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `foto_candidato` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      PRIMARY KEY (`id_candidato`) USING BTREE
      ) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;''')

TABLES['ComiteElectoral'] = ('''
      CREATE TABLE `comite_electoral`  (
      `id_comite` int NOT NULL,
      `ci_comite` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `contrasena` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      PRIMARY KEY (`id_comite`) USING BTREE
      ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;''')

TABLES['Elector'] = ('''
      CREATE TABLE `elector`  (
      `ci_elector` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `apellido_paterno` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `apellido_materno` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      `fecha_nacimiento` date NOT NULL,
      `estado` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
      PRIMARY KEY (`ci_elector`) USING BTREE
      ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;''')

TABLES['Voto'] = ('''
     CREATE TABLE `voto`  (
      `id_voto` int NOT NULL AUTO_INCREMENT,
      `ci_elector` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
      `id_candidato` int NULL DEFAULT NULL,
      PRIMARY KEY (`id_voto`) USING BTREE,
      INDEX `ci_elector`(`ci_elector` ASC) USING BTREE,
      INDEX `id_candidato`(`id_candidato` ASC) USING BTREE,
      CONSTRAINT `ci_elector` FOREIGN KEY (`ci_elector`) REFERENCES `elector` (`ci_elector`) ON DELETE RESTRICT ON UPDATE RESTRICT,
      CONSTRAINT `id_candidato` FOREIGN KEY (`id_candidato`) REFERENCES `candidato` (`id_candidato`) ON DELETE RESTRICT ON UPDATE RESTRICT
      ) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;''')

for tabla_nombre in TABLES:
      tabla_sql = TABLES[tabla_nombre]
      try:
            print('Creando tabla {}:'.format(tabla_nombre), end=' ')
            cursor.execute(tabla_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Ya existe la tabla')
            else:
                  print(err.msg)
      else:
            print('OK')


usuario_sql = 'INSERT INTO elector (ci_elector, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, estado ) VALUES (%s, %s, %s,%s, %s, %s)'

usuarios = [
      ('111', 'Rick', 'Sanchez', "Smith", "09-09-09", "habilitado" ),
      ('222', 'Alvin', 'Martinez', "Flores", "08-08-08", "habilitado" ),
      ('333', 'Bruno', 'Diaz', "Wayne", "07-07-07", "habilitado" ),
      ('444', 'Barry', 'Allen', "Ford", "05-05-05", "desahibilitado" ),
      ('555', 'Ana', 'Rodriguez', "Vargas", "04-04-04", "habilitado" )
]
cursor.executemany(usuario_sql, usuarios)

candi = 'INSERT INTO candidato(id_candidato, nombre_partido, nombre_candidato, foto_candidato) VALUES (%s, %s, %s,%s)'
cad = [
    ('11','INAPJA/XYZ','Jeanine Aniez','/assets/asdias.jpg'),
    ('22','XYZ/CHI','Chi','/assetes/chi.jpg' ),
    ('33','MAU/XZA','Maurio Monzon','/assets/mau.jpg'),
    ('44', 'MCO/PCO','Luis Mesa','/assets/ms.jpg'),
    ('0','none','Blanco','/assets/blanco.jpg'),
    ('1','none','Nulo','/assets/nulo.jpg')
]
cursor.executemany(candi, cad)

admin = 'INSERT INTO administrador(id_admin, username, contrasena) VALUES (%s, %s, %s)'
ad = [
    ('1','admin','admin')
]
cursor.executemany(admin, ad)
#Cambiar por ruta


# commitando si no hay nada que tenga efecto
conn.commit()

cursor.close()
conn.close()


# comite1 = Comite_electoral('jose', 1, 'qwe')
# comite2 = Comite_electoral('pablo', 123457, 'password')

# comites=[comite1,comite2] # Lista de comite
# candidatos = []
# candidato1 = Candidato('javier milei',97, 'KML','images/baner.jpg')
# candidato2 = Candidato('sergio massa',98, 'XYZ','images/yoo.JPG')
# candidato3 = Candidato('patricia bullrich',99, 'RQT','images/yoo.JPG')
# candidatos=[candidato1, candidato2, candidato3]   # lista de candidatos

# elector1 = Elector('Mauricio Nestor',1,'no habilitado','2003-09-20','Apaza','Callapa')
# elector2 = Elector('Miguel Grover',2, 'habilitado', '2003-09-20','Mita','gueon')
# elector3 = Elector('luis cuadros',3, 'habilitado','2003-09-20','perez', 'aeaon' )

# electores=[elector1, elector2, elector3]   # lista de electores

# votos =[]  # lista de votos



from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from elector import Elector
from candidato import Candidato
from comite_electoral import Comite_electoral
from voto import Voto


comite1 = Comite_electoral('jose', 1, 'qwe')
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

app = Flask(__name__)
app.secret_key = 'cochabamba'

app.config['SQLALCHEMY_DATABASE_URI'] = \
'{SGBD}://{usuario}:{clave}@{servidor}/{database}'.format(
SGBD = 'mysql+mysqlconnector',
usuario = 'MauriApaza845',
clave = 'Mauricio67532900',
#clave = 'admin',
servidor = 'MauriApaza845.mysql.pythonanywhere-services.com',
database = 'MauriApaza845$sistemaEleccionesDB'
)
db = SQLAlchemy(app)


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







def obtener_lista_de_electores():
    return electores


@app.route('/irVotar', methods=['POST'])
def irVotar():
    electores = obtener_lista_de_electores()

    return render_template('votar.html', candidatos=candidatos, electores=electores)




@app.route('/realizar_votacion', methods=['POST'])
def realizar_votacion():
    elector_ci = request.form.get('elector_ci')
    candidato_ci = request.form.get('candidato_ci')

    for elector in electores:
        if str(elector.get_ci())==elector_ci:
            elector.habilitado.setter('no habilitado')
            for candidato in candidatos:
                if str(candidato.get_ci()) == candidato_ci:
                    candidato.aumentar_votos()
                    flash('¡Tu voto ha sido registrado!', 'success')
                    return render_template('loginUsuario.html')


    return render_template('verResultados.html', candidatos=candidatos)


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
            return render_template('verResultados.html', candidatos=candidatos)

    if not registrado:
        flash('CI y/o Contraseña incorrecta, por favor vuelve a ingresar los datos.', 'error')

    return render_template('loginComite.html', candidatos=candidatos)



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