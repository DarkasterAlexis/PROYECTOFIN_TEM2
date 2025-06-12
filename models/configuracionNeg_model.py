from database import db

class ConfiguracionNegocio(db.Model):
    __tablename__ = "confnegocios"
    id = db.Column(db.Integer, primary_key=True)
    nombreparametro = db.Column(db.String(50), nullable=False)
    valorparametro = db.Column(db.String(100), nullable=False)

    def __init__(self, nombreparametro, valorparametro):
        self.nombreparametro = nombreparametro
        self.valorparametro = valorparametro

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ConfiguracionNegocio.query.all()

    @staticmethod
    def get_by_id(id):
        return ConfiguracionNegocio.query.get(id)

    def update(self, nombreparametro=None, valorparametro=None):
        if nombreparametro and valorparametro:
            self.nombreparametro = nombreparametro
            self.valorparametro = valorparametro
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
