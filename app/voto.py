from candidato import Candidato

class Voto:
    def __init__(self,candidato:Candidato):
        self.__candidato = candidato

    @property
    def get_candidato(self):
        return self.__candidato


    def emitir_voto(self):
        if self.__elector.habilitado:
            self.__elector.habilitado = False
        else:
            print('Usted {} ya realizó su voto ... estado habilitación:{}'.format(self.__elector.get_nombre(), False ))
