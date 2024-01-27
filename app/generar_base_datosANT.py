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


# insertando usuarios
usuario_sql = 'INSERT INTO elector (ci_elector, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, estado ) VALUES (%s, %s, %s,%s, %s, %s)'

usuarios = [
      ('123', 'Armando', 'Esteban', "Quito", "10-10-10", "habilitado" )
]
cursor.executemany(usuario_sql, usuarios)
#Cambiar por ruta
cursor.execute('select * from MauriApaza845$sistemaEleccionesDB.elector')
print(' -------------  Usuarios:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando si no hay nada que tenga efecto
conn.commit()

cursor.close()
conn.close()