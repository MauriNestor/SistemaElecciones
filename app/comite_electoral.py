from persona import Persona

class Comite_electoral(Persona):
    def __init__(self, nombre, ci, contrasena):
        super().__init__(nombre, ci)
        self.__contrasena = contrasena
        self.__ci = ci

    @property
    def get_contrasena(self):
        return self.__contrasena