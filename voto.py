class Voto(db.Model):
    id_voto = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ci_elector = db.Column(db.String(8), db.ForeignKey('ci_elector'), nullable=False)
    id_candidato = db.Column(db.String(8), db.ForeignKey('id_candidato'), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name
        
    def votar(self, candidato):
        # Verificar si el elector está habilitado para votar
        if not self.habilitado:
            return "El elector no está habilitado para votar."

        # Verificar si el candidato existe
        if not Candidato.query.get(candidato.id):
            return "El candidato seleccionado no existe."

        # Verificar si el elector ya ha votado por este candidato
        if Voto.query.filter_by(cod_elector=self.id, cod_candidato=candidato.id).first():
            return "El elector ya ha votado por este candidato."

        # Crear un nuevo voto
        nuevo_voto = Voto(ci_elector=self.ci_elector, id_candidato=candidato.id_candidato)
        db.session.add(nuevo_voto)
        db.session.commit()