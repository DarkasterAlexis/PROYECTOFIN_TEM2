from database import db

class Cliente(db.Model):
    __tablename__ = "clientes"  # El nombre de la tabla en la base de datos

    clienteID = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)  # email es único
    telefono = db.Column(db.String(20), nullable=False)
    contrasenaHash = db.Column(db.String(255), nullable=True) # Puede ser nulo si no tiene cuenta

    def __init__(self, nombre, apellido, email, telefono, contrasenaHash=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.contrasenaHash = contrasenaHash

    def save(self):
        """Guarda un nuevo cliente en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Obtiene todos los clientes de la base de datos."""
        return Cliente.query.all()

    @staticmethod
    def get_by_id(id):
        """Obtiene un cliente por su ID."""
        return Cliente.query.get(id)

    @staticmethod
    def get_by_email(email):
        """Obtiene un cliente por su dirección de correo electrónico."""
        return Cliente.query.filter_by(email=email).first()

    def update(self, nombre=None, apellido=None, email=None, telefono=None, contrasenaHash=None):
        """Actualiza la información de un cliente existente."""
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if email: self.email = email
        if telefono: self.telefono = telefono
        if contrasenaHash: self.contrasenaHash = contrasenaHash
        db.session.commit()

    def delete(self):
        """Elimina un cliente de la base de datos."""
        db.session.delete(self)
        db.session.commit()