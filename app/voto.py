class Voto:
    def __init__(self, elector, voto):
        self.__elector = elector
        self.__voto = voto

    @property
    def voto(self):
        return self.__voto

    def emitir_voto(self):
        if self.__elector.habilitado:
            self.__elector.habilitado = False
        else:
            print('Usted {} ya realizó su voto ... estado habilitación:{}'.format(self.__elector.get_nombre(), False ))