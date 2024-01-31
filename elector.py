from app import db

class Elector(db.Model):
    ci_elector = db.Column(db.String(8), primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido_paterno = db.Column(db.String(80), nullable=False)
    apellido_materno = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(80), nullable=False)

    def __init__(self, ci_elector, nombre, apellido_paterno, apellido_materno, estado, fecha_nacimiento):
        self.__nombre = nombre
        self.__fechaNacimiento = fechaNacimiento
        self.__estado = estado
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno

    @property
    def es_habilitado(self):
        return self.__habilitado
    @property
    def fnacmiento(self):
        return self.__fechaNacimiento
    @property
    def apellidoPaterno(self):
        return self.__apellido1

    @property
    def apellidoMaterno(self):
        return self.__apellido2

    @es_habilitado.setter
    def es_habilitado(self, valor):
        self.__habilitado = valor


