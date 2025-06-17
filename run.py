from flask import Flask, request,render_template,redirect,url_for
from controllers import configuracionNeg_controller,historialcambres_controller,notificaciones_controller,servicio_controller
from flask_login import LoginManager,login_required, logout_user, login_user,UserMixin,current_user
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pedidos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(configuracionNeg_controller.configuracion_bp)
app.register_blueprint(historialcambres_controller.historial_bp)
app.register_blueprint(notificaciones_controller.notificaciones_bp)
app.register_blueprint(servicio_controller.servicios_bp)

@app.route("/")
def home():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)