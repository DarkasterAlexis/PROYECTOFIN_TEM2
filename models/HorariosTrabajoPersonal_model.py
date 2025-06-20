from database import db

class HorariosTrabajoPersonal(db.Model):
    _tablename_ = "horariostrabajopersonal"

    HorarioID = db.Column(db.Integer, primary_key=True)
    PersonalID = db.Column(db.Integer, db.ForeignKey("personal.PersonalID"), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)
    HoraEntrada = db.Column(db.Time, nullable=False)
    HoraSalida = db.Column(db.Time, nullable=False)
    DiaSemana = db.Column(db.String(20), nullable=False)

    def _init_(self, PersonalID, Fecha, HoraEntrada, HoraSalida, DiaSemana):
        self.PersonalID = PersonalID
        self.Fecha = Fecha
        self.HoraEntrada = HoraEntrada
        self.HoraSalida = HoraSalida
        self.DiaSemana = DiaSemana

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return HorariosTrabajoPersonal.query.all()

    @staticmethod
    def get_by_id(id):
        return HorariosTrabajoPersonal.query.get(id)

    def update(self, Fecha=None, HoraEntrada=None, HoraSalida=None, DiaSemana=None):
        if Fecha: self.Fecha = Fecha
        if HoraEntrada: self.HoraEntrada = HoraEntrada
        if HoraSalida: self.HoraSalida = HoraSalida
        if DiaSemana: self.DiaSemana = DiaSemana
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()