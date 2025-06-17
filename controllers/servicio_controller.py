from flask import Blueprint, request, jsonify
from database import db
from models import Servicio

servicios_bp = Blueprint('servicios_bp', __name__)

@servicios_bp.route('/servicios', methods=['POST'])
def crear_servicio():
    data = request.json
    servicio = Servicio(
        nombre_servicio=data['nombre_servicio'],
        descripcion=data['descripcion'],
        duracion_default=data['duracion_default'],
        precio=data.get('precio')
    )
    db.session.add(servicio)
    db.session.commit()
    return jsonify({'message': 'Servicio creado', 'servicio_id': servicio.servicio_id}), 201

@servicios_bp.route('/servicios', methods=['GET'])
def listar_servicios():
    servicios = Servicio.query.all()
    resultado = [
        {
            'servicio_id': s.servicio_id,
            'nombre_servicio': s.nombre_servicio,
            'descripcion': s.descripcion,
            'duracion_default': s.duracion_default,
            'precio': str(s.precio) if s.precio else None
        }
        for s in servicios
    ]
    return jsonify(resultado)

@servicios_bp.route('/servicios/<int:servicio_id>', methods=['PUT'])
def actualizar_servicio(servicio_id):
    servicio = Servicio.query.get_or_404(servicio_id)
    data = request.json
    servicio.nombre_servicio = data.get('nombre_servicio', servicio.nombre_servicio)
    servicio.descripcion = data.get('descripcion', servicio.descripcion)
    servicio.duracion_default = data.get('duracion_default', servicio.duracion_default)
    servicio.precio = data.get('precio', servicio.precio)
    db.session.commit()
    return jsonify({'message': 'Servicio actualizado'})

@servicios_bp.route('/servicios/<int:servicio_id>', methods=['DELETE'])
def eliminar_servicio(servicio_id):
    servicio = Servicio.query.get_or_404(servicio_id)
    db.session.delete(servicio)
    db.session.commit()
    return jsonify({'message': 'Servicio eliminado'})
