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