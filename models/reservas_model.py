from database import db

class Reserva(db.Model):
    _tablename_ = "reservas"

    ReservaID = db.Column(db.Integer, primary_key=True)
    ClienteID = db.Column(db.Integer, nullable=False)
    RecursoID = db.Column(db.Integer, nullable=False)
    FechaReserva = db.Column(db.Date, nullable=False)
    HoraInicio = db.Column(db.Time, nullable=False)
    HoraFin = db.Column(db.Time, nullable=False)
    NumeroPersonas = db.Column(db.Integer)
    TipoCita = db.Column(db.String(100))
    EstadoReserva = db.Column(db.String(50))
    FechaCreacion = db.Column(db.DateTime)
    NotasCliente = db.Column(db.Text)

    def _init_(self, ClienteID, RecursoID, FechaReserva, HoraInicio, HoraFin,
                 NumeroPersonas=None, TipoCita=None, EstadoReserva=None,
                 FechaCreacion=None, NotasCliente=None):
        self.ClienteID = ClienteID
        self.RecursoID = RecursoID
        self.FechaReserva = FechaReserva
        self.HoraInicio = HoraInicio
        self.HoraFin = HoraFin
        self.NumeroPersonas = NumeroPersonas
        self.TipoCita = TipoCita
        self.EstadoReserva = EstadoReserva
        self.FechaCreacion = FechaCreacion
        self.NotasCliente = NotasCliente

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Reserva.query.all()

    @staticmethod
    def get_by_id(id):
        return Reserva.query.get(id)

    def update(self, ClienteID=None, RecursoID=None, FechaReserva=None, HoraInicio=None, HoraFin=None,
               NumeroPersonas=None, TipoCita=None, EstadoReserva=None, FechaCreacion=None, NotasCliente=None):
        # Actualizar solo si todos los parámetros obligatorios están presentes
        if ClienteID is not None and RecursoID is not None and FechaReserva is not None and HoraInicio is not None and HoraFin is not None:
            self.ClienteID = ClienteID
            self.RecursoID = RecursoID
            self.FechaReserva = FechaReserva
            self.HoraInicio = HoraInicio
            self.HoraFin = HoraFin

            # Campos opcionales, actualizar solo si no son None
            if NumeroPersonas is not None:
                self.NumeroPersonas = NumeroPersonas
            if TipoCita is not None:
                self.TipoCita = TipoCita
            if EstadoReserva is not None:
                self.EstadoReserva = EstadoReserva
            if FechaCreacion is not None:
                self.FechaCreacion = FechaCreacion
            if NotasCliente is not None:
                self.NotasCliente = NotasCliente

            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()