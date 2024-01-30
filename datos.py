import mysql.connector
from mysql.connector import errorcode

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


# insertando usuarios
usuario_sql = 'INSERT INTO elector (ci_elector, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, estado ) VALUES (%s, %s, %s,%s, %s, %s)'

usuarios = [
      ('111', 'Rick', 'Sanchez', "Smith", "09-09-09", "habilitado" ),
      ('222', 'Alvin', 'Martinez', "Flores", "08-08-08", "habilitado" ),
      ('333', 'Bruno', 'Diaz', "Wayne", "07-07-07", "habilitado" ),
      ('444', 'Barry', 'Allen', "Ford", "05-05-05", "desahibilitado" ),
      ('555', 'Ana', 'Rodriguez', "Vargas", "04-04-04", "habilitado" )
]
cursor.executemany(usuario_sql, usuarios)

candi = 'INSERT INTO candidato(id_candidato, nombre_partido, nombre_candidato, foto_candidato)'
cad = [
    ('11','INAPJA/XYZ','Jeanine Aniez','/assets/asdias.jpg'),
    ('22','XYZ/CHI','Chi','/assetes/chi.jpg' ),
    ('33','MAU/XZA','Maurio Monzon','/assets/mau.jpg'),
    ('44', 'MCO/PCO','Luis Mesa','/assets/ms.jpg'),
    ('0','none','Blanco','/assets/blanco.jpg'),
    ('1','none','Nulo','/assets/nulo.jpg')
]
cursor.executemany(candi, cad)

admin = 'INSERT INTO administrador(id_admin, username, contrasena)'
ad = [
    ('1','admin','admin')
]
cursor.executemany(admin, ad)
#Cambiar por ruta


# commitando si no hay nada que tenga efecto
conn.commit()

cursor.close()
conn.close()