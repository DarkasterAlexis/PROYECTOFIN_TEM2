from database import db

class Personal(db.Model):
    _tablename_ = "personal"

    PersonalID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Apellido = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20),nullable=False)
    Rol = db.Column(db.String(50), nullable=False)

    def _init_(self, Nombre, Apellido, Email, Telefono,password, Rol):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Email = Email
        self.Telefono = Telefono
        self.password=password
        self.Rol = Rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Personal.query.all()

    @staticmethod
    def get_by_id(id):
        return Personal.query.get(id)

    def update(self, Nombre=None, Apellido=None, Email=None, Telefono=None,password=None, Rol=None):
        if Nombre and Apellido and Email and Telefono and password and Rol:
                self.Nombre = Nombre
                self.Apellido = Apellido
                self.Email = Email
                self.Telefono = Telefono
                self.password = password
                self.Rol = Rol
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()