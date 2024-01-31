from app import db

class Candidato(db.Model):
    id_candidato = db.Column(db.String(8), primary_key=True)
    nombre_candidato = db.Column(db.String(50), nullable=False)
    nombre_partido = db.Column(db.String(20), nullable=False)
    foto_candidato = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre_candidato, nombre_partido):
        self.__nombre_candidato = nombre_candidato
        self.__nombre_partido = nombre_partido

    def contar_votos(self):
        return db.session.query(func.count(Voto.id_voto)).filter_by(id_candidato=self.id_candidato).scalar()