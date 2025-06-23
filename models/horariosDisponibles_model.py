from database import db
from datetime import date, time # Importar para los tipos DATE y TIME

class HorarioDisponible(db.Model):
    __tablename__ = "horarios_disponibles" # El nombre de la tabla en la base de datos

    slotID = db.Column(db.Integer, primary_key=True)
    recursoID = db.Column(db.Integer, db.ForeignKey('recursos.recursoID'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    horaInicio = db.Column(db.Time, nullable=False)
    horaFin = db.Column(db.Time, nullable=False)
    estaDisponible = db.Column(db.Boolean, default=True, nullable=False) # Valor por defecto a True
    notas = db.Column(db.Text, nullable=True)

    # Relación con la tabla Recursos (opcional pero recomendable para una buena práctica)
    recurso = db.relationship('Recurso', backref='horarios_disponibles')

    def __init__(self, recursoID, fecha, horaInicio, horaFin, estaDisponible=True, notas=None):
        self.recursoID = recursoID
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.estaDisponible = estaDisponible
        self.notas = notas

    def save(self):
        """Guarda un nuevo horario disponible en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Obtiene todos los horarios disponibles de la base de datos."""
        return HorarioDisponible.query.all()

    @staticmethod
    def get_by_id(id):
        """Obtiene un horario disponible por su ID."""
        return HorarioDisponible.query.get(id)

    @staticmethod
    def get_available_slots_for_resource_and_date(recurso_id, fecha):
        """Obtiene slots disponibles para un recurso y fecha específicos."""
        return HorarioDisponible.query.filter_by(
            recursoID=recurso_id,
            fecha=fecha,
            estaDisponible=True
        ).all()

    def update(self, recursoID=None, fecha=None, horaInicio=None, horaFin=None, estaDisponible=None, notas=None):
        """Actualiza la información de un horario disponible existente."""
        if recursoID: self.recursoID = recursoID
        if fecha: self.fecha = fecha
        if horaInicio: self.horaInicio = horaInicio
        if horaFin: self.horaFin = horaFin
        if estaDisponible is not None: self.estaDisponible = estaDisponible # Booleano puede ser False
        if notas is not None: self.notas = notas
        db.session.commit()

    def delete(self):
        """Elimina un horario disponible de la base de datos."""
        db.session.delete(self)
        db.session.commit()