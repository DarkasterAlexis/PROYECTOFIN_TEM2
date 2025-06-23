from flask import Blueprint, request, redirect, url_for
from models.usuarios_model import Usuario
from werkzeug.security import generate_password_hash
from views import usuarios_view  # Aquí se importa

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