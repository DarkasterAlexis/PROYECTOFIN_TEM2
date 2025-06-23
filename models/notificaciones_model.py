from database import db
from datetime import datetime

class Notificacion(db.Model):
    __tablename__ = "notificaciones"
    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer,nullable=False)
    tiponotificacion = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.String(255), nullable=False)
    fechaenvio = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    estadoenvio = db.Column(db.String(20), nullable=False)

    def __init__(self,reserva_id, tiponotificacion, mensaje, fechaenvio, estadoenvio):
        self.reserva_id=reserva_id
        self.tiponotificacion = tiponotificacion
        self.mensaje = mensaje
        self.fechaenvio = fechaenvio
        self.estadoenvio = estadoenvio

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Notificacion.query.all()

    @staticmethod
    def get_by_id(id):
        return Notificacion.query.get(id)

    def update(self,reserva_id=None, tiponotificacion=None, mensaje=None, fechaenvio=None, estadoenvio=None):
        if  reserva_id and tiponotificacion and mensaje and fechaenvio and estadoenvio:
            self.reserva_id=reserva_id
            self.tiponotificacion = tiponotificacion
            self.mensaje = mensaje
            self.fechaenvio = fechaenvio
            self.estadoenvio = estadoenvio
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
