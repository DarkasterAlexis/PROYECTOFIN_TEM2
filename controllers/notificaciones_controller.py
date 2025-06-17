from flask import Blueprint, request, jsonify
from database import db
from models import Notificacion

notificaciones_bp = Blueprint('notificaciones_bp', __name__)

@notificaciones_bp.route('/notificaciones', methods=['POST'])
def crear_notificacion():
    data = request.json
    notificacion = Notificacion(
        reserva_id=data['reserva_id'],
        tipo_notificacion=data['tipo_notificacion'],
        mensaje=data['mensaje'],
        estado_envio=data['estado_envio']
    )
    db.session.add(notificacion)
    db.session.commit()
    return jsonify({'message': 'Notificación creada', 'notificacion_id': notificacion.notificacion_id}), 201

@notificaciones_bp.route('/notificaciones/<int:notificacion_id>', methods=['PUT'])
def actualizar_notificacion(notificacion_id):
    notificacion = Notificacion.query.get_or_404(notificacion_id)
    data = request.json
    notificacion.tipo_notificacion = data.get('tipo_notificacion', notificacion.tipo_notificacion)
    notificacion.mensaje = data.get('mensaje', notificacion.mensaje)
    notificacion.estado_envio = data.get('estado_envio', notificacion.estado_envio)
    db.session.commit()
    return jsonify({'message': 'Notificación actualizada'})

@notificaciones_bp.route('/notificaciones/<int:notificacion_id>', methods=['DELETE'])
def eliminar_notificacion(notificacion_id):
    notificacion = Notificacion.query.get_or_404(notificacion_id)
    db.session.delete(notificacion)
    db.session.commit()
    return jsonify({'message': 'Notificación eliminada'})
