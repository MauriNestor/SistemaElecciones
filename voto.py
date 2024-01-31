from flask_sqlalchemy import SQLAlchemy
from candidato import Candidato
from elector import Elector

db = SQLAlchemy()

class Voto(db.Model):
    id_voto = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_elector = db.Column(db.Integer, db.ForeignKey('elector.id'), nullable=False)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)

    def __init__(self, cod_elector, cod_candidato):
        self.__cod_elector = cod_elector
        self.__cod_candidato = cod_candidato