from persona import Persona

class Candidato(Persona):
    def __init__(self, nombre, ci, partido, imagen):
        super().__init__(nombre, ci)
        self.__partido = partido
        self.__imagen = imagen
        self.__votos = 0

    def get_partido(self):
        return self.__partido

    @property
    def imagen(self):
        return self.__imagen

    @property
    def votos(self):
        return self.__votos


    def aumentar_votos(self):
        self.__votos += 1
