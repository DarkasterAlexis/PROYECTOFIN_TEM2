from flask import Blueprint, request,redirect,url_for
from models.servicio_model import Servicio
from views import servicio_view

servicios_bp = Blueprint('servicio', __name__,url_prefix="/servicios")

@servicios_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre_servicio=request.form['nombre_servicio']
        descripcion=request.form['descripcion']
        duraciondefault=request.form['duraciondefault']
        precio=request.form['precio']
        servicio = Servicio(nombre_servicio,descripcion,duraciondefault,precio)
        servicio.save()
        return redirect(url_for('servicio.index'))
    return servicio_view.create()

# @servicios_bp.route('/servicios', methods=['GET'])
# def listar_servicios():
#     servicios = servicio_model.query.all()
#     resultado = [
#         {
#             'servicio_id': s.servicio_id,
#             'nombre_servicio': s.nombre_servicio,
#             'descripcion': s.descripcion,
#             'duracion_default': s.duracion_default,
#             'precio': str(s.precio) if s.precio else None
#         }
#         for s in servicios
#     ]
#     return jsonify(resultado)

@servicios_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    servicio = Servicio.get_by_id(id)
    if request.method == 'POST':
        nombre_servicio=request.form['nombre_servicio']
        descripcion=request.form['descripcion']
        duraciondefault=request.form['duraciondefault']
        precio=request.form['precio']
        servicio.update(nombre_servicio=nombre_servicio,descripcion=descripcion,duraciondefault=duraciondefault,precio=precio)
        return redirect(url_for('servicio.index'))
    return servicio_view.create()

@servicios_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    servicio = Servicio.get_by_id(id)
    servicio.delete(servicio)
    return redirect(url_for('servicio.index'))
