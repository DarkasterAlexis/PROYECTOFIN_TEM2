from database import db
from flask_login import UserMixin

class Personal(db.Model,UserMixin):
    _tablename_ = "personal"
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20),nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __init__(self, Nombre, Apellido, email, Telefono, password, rol):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.email = email
        self.Telefono = Telefono
        self.password=password
        self.rol = rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Personal.query.all()

    @staticmethod
    def get_by_id(id):
        return Personal.query.get(id)

    def update(self, Nombre=None, Apellido=None, email=None, Telefono=None,password=None, rol=None):
        if Nombre and Apellido and email and Telefono and password and rol:
                self.Nombre = Nombre
                self.Apellido = Apellido
                self.email = email
                self.Telefono = Telefono
                self.password = password
                self.rol = rol
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()