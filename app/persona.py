
class Persona:
    def __init__(self, nombre, ci):
        self.__nombre = nombre.title()
        self.__ci = ci

    def get_nombre(self):
        return self.__nombre

    def get_ci(self):
        return self.__ci
