from flask import Flask, request,render_template,redirect,url_for
from controllers import configuracionNeg_controller,historialcambres_controller,notificaciones_controller,servicio_controller,HorariosTrabajoPersonal_controller,reservas_controller,personal_controller,usuarios_controller,clientes_controller,recursos_controller,horariosDisponibles_controller
from flask_login import LoginManager,login_required, logout_user, login_user,UserMixin,current_user
from database import db
from models.clientes_model import Cliente

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pedidos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.secret_key = 'Darkaster_7024'
login_manager = LoginManager()
login_manager.login_view = 'usuario.login'
login_manager.init_app(app)
app.debug=True

app.register_blueprint(configuracionNeg_controller.configuracion_bp)
app.register_blueprint(historialcambres_controller.historial_bp)
app.register_blueprint(notificaciones_controller.notificaciones_bp)
app.register_blueprint(servicio_controller.servicios_bp)
app.register_blueprint(HorariosTrabajoPersonal_controller.horarios_bp)
app.register_blueprint(reservas_controller.reserva_bp)
app.register_blueprint(personal_controller.personal_bp)
app.register_blueprint(usuarios_controller.usuario_bp)
app.register_blueprint(clientes_controller.cliente_bp)
app.register_blueprint(recursos_controller.recurso_bp)
app.register_blueprint(horariosDisponibles_controller.horario_disponible_bp)


@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return (dict(is_active = is_active))

@login_manager.user_loader
def load_user(user_id):
    return Cliente.get_by_id(user_id)

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)