from database import db
from datetime import datetime

class HistorialCambioReserva(db.Model):
    __tablename__ = "histcambreservas"
    id = db.Column(db.Integer, primary_key=True)
    reser_id = db.Column(db.Integer,nullable=False)
    campomodificado = db.Column(db.String(50), nullable=False)
    valorantiguo = db.Column(db.String(100), nullable=False)
    valornuevo = db.Column(db.String(100), nullable=False)
    fechacambio = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuariomodifi_id=db.Column(db.Integer,nullable=False)

    def __init__(self,reser_id, campomodificado, valorantiguo, valornuevo, fechacambio,usuariomodifi_id):
        self.reser_id = reser_id
        self.campomodificado = campomodificado
        self.valorantiguo = valorantiguo
        self.valornuevo = valornuevo
        self.fechacambio = fechacambio
        self.usuariomodifi_id=usuariomodifi_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return HistorialCambioReserva.query.all()

    @staticmethod
    def get_by_id(id):
        return HistorialCambioReserva.query.get(id)

    # def update(self,reser_id=None, campomodificado=None, valorantiguo=None, valornuevo=None, fechacambio=None):
    #     if campomodificado and valorantiguo and valornuevo and fechacambio:
    #         self.campomodificado = campomodificado
    #         self.valorantiguo = valorantiguo
    #         self.valornuevo = valornuevo
    #         self.fechacambio = fechacambio
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
