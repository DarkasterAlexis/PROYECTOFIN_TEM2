from flask import Blueprint, request, redirect, url_for
from models.personal_model import Personal
from models.usuarios_model import Usuario
from views import personal_view
from werkzeug.security import generate_password_hash

personal_bp = Blueprint('personal', __name__, url_prefix="/personal")

@personal_bp.route("/")
def index():
    personal_list = Personal.get_all()
    return personal_view.list(personal_list)

@personal_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        email = request.form['Email']
        telefono = request.form['Telefono']
        password = request.form['password']
        rol = request.form['Rol']
        persona = Personal(nombre, apellido, email, telefono,password, rol)
        persona.save()       
        usuario = Usuario(
            Nombre =nombre,
            Apellido = apellido,
            Email = email,
            Telefono = telefono,
            password = generate_password_hash(password),
            idtipouser = persona.id,
            tiprelacion = "personal",
            Rol = rol
        )
        usuario.save()    
        return redirect(url_for('personal.index'))
    return personal_view.create()

@personal_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    persona = Personal.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        email = request.form['Email']
        telefono = request.form['Telefono']
        password = request.form['password']
        rol = request.form['Rol']

        persona.update(nombre, apellido, email, telefono,password, rol)
        return redirect(url_for('personal.index'))
    return personal_view.edit(persona)

@personal_bp.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    persona = Personal.get_by_id(id)
    persona.delete()
    return redirect(url_for('personal.index'))
