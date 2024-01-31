
from persona import Persona

class Elector(Persona):
    def __init__(self, nombre, ci, habilitado,fechaNacimiento, apellido1,apellido2):
        super().__init__(nombre, ci)
        self.__fechaNacimiento = fechaNacimiento
        self.__habilitado = habilitado
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2

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


