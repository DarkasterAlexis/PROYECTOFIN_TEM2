from database import db

class Recurso(db.Model):
    __tablename__ = "recursos"  # El nombre de la tabla en la base de datos

    recursoID = db.Column(db.Integer, primary_key=True)
    nombreRecurso = db.Column(db.String(100), nullable=False)
    tipoRecurso = db.Column(db.String(50), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text, nullable=True) # TEXT en SQLAlchemy se mapea a Text

    def __init__(self, nombreRecurso, tipoRecurso, capacidad, descripcion=None):
        self.nombreRecurso = nombreRecurso
        self.tipoRecurso = tipoRecurso
        self.capacidad = capacidad
        self.descripcion = descripcion

    def save(self):
        """Guarda un nuevo recurso en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Obtiene todos los recursos de la base de datos."""
        return Recurso.query.all()

    @staticmethod
    def get_by_id(id):
        """Obtiene un recurso por su ID."""
        return Recurso.query.get(id)

    def update(self, nombreRecurso=None, tipoRecurso=None, capacidad=None, descripcion=None):
        """Actualiza la información de un recurso existente."""
        if nombreRecurso: self.nombreRecurso = nombreRecurso
        if tipoRecurso: self.tipoRecurso = tipoRecurso
        if capacidad is not None: self.capacidad = capacidad # capacidad puede ser 0, por eso la verificación
        if descripcion is not None: self.descripcion = descripcion # La descripción puede ser una cadena vacía
        db.session.commit()

    def delete(self):
        """Elimina un recurso de la base de datos."""
        db.session.delete(self)
        db.session.commit()