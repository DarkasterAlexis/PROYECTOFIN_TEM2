from database import db

class Servicio(db.Model):
    __tablename__ = "servicios"
    id = db.Column(db.Integer,primary_key = True)
    nombre_servicio = db.Column(db.String(20),nullable=False)
    descripcion = db.Column(db.String(150),nullable=False)
    duraciondefault = db.Column(db.Integer,nullable=False)
    precio = db.Column(db.Float(11,2),nullable=False)
    
    def __init__(self,nombre_servicio,descripcion,duraciondefault,precio):
        self.nombre_servicio=nombre_servicio
        self.descripcion=descripcion
        self.duraciondefault=duraciondefault
        self.precio=precio
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Servicio.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Servicio.query.get(id)
    
    def update(self,nombre_servicio=None,descripcion=None,duraciondefalut=None,precio=None):
        if nombre_servicio and descripcion and duraciondefalut and precio:
            self.nombre_servicio=nombre_servicio
            self.descripcion=descripcion
            self.duraciondefault=duraciondefalut
            self.precio=precio
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
            