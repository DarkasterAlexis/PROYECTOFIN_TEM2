from database import db
from flask_login import UserMixin

class Usuario(db.Model,UserMixin):
    _tablename_ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String,nullable=False)
    idtipouser = db.Column(db.Integer,nullable=False)
    tiprelacion = db.Column(db.String(20),nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __init__(self, Nombre, Apellido, email, Telefono,password,idtipouser,tiprelacion, rol):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.email = email
        self.Telefono = Telefono
        self.password=password
        self.idtipouser=idtipouser
        self.tiprelacion=tiprelacion
        self.rol = rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    def update(self, Nombre=None, Apellido=None, email=None, Telefono=None,password=None,idtipouser=None,tiprelacion=None, rol=None):
        if Nombre and Apellido and email and Telefono and password and idtipouser and tiprelacion and rol:
            self.Nombre = Nombre
            self.Apellido = Apellido
            self.email = email
            self.Telefono = Telefono
            self.password= password
            self.idtipouser= idtipouser
            self.tiprelacion=tiprelacion
            self.rol = rol
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def get_by_email(email):
        """Obtiene un cliente por su dirección de correo electrónico."""
        return Usuario.query.filter_by(email=email).first()