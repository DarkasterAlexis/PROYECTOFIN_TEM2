from flask import Blueprint, request, redirect, url_for,flash,render_template
from models.usuarios_model import Usuario
from werkzeug.security import generate_password_hash,check_password_hash
from views import usuarios_view  # Aquí se importa
from flask_login import login_user,login_required,logout_user,current_user

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")

@usuario_bp.route('/')
def index():
    usuarios = Usuario.get_all()
    return usuarios_view.list(usuarios)  # Aquí se llama la vista

@usuario_bp.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))

@usuario_bp.route("/login",methods=['GET','POST'])
def login():
    next_page = request.args.get('next')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.get_by_email(email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.rol == "client":
                return redirect(next_page or url_for("usuario.dashboard"))
            elif user.rol == "person":
                return redirect(next_page or url_for("usuario.inicioperson"))
            elif user.rol == "admin":
                flash('INICIO DE SESION EXITOSO','success')
                return redirect(next_page or url_for("usuario.inicioadmin"))
            else:
                flash("Correo o la contraseña estan incorrectos :(")
                return render_template("login/login.html")
        else:
            flash('Credenciales Invalidas','danger')
    return usuarios_view.login(next_page)

@usuario_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("usuario.login"))

@usuario_bp.route("/dashboard")
@login_required
def dashboard():
    return usuarios_view.dashboard(current_user)

@usuario_bp.route("/inicioperson")
@login_required
def inicioperson():
    return usuarios_view.inicioperson(current_user)

@usuario_bp.route("/inicioadmin")
@login_required
def inicioadmin():
    return usuarios_view.inicioadmin(current_user)