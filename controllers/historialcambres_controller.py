from flask import Blueprint, request, jsonify
from database import db
from models import HistorialReserva

historial_bp = Blueprint('historial_bp', __name__)

@historial_bp.route('/historial', methods=['POST'])
def crear_historial():
    data = request.json
    historial = HistorialReserva(
        reserva_id=data['reserva_id'],
        campo_modificado=data['campo_modificado'],
        valor_antiguo=data.get('valor_antiguo'),
        valor_nuevo=data.get('valor_nuevo'),
        usuario_modificador_id=data['usuario_modificador_id']
    )
    db.session.add(historial)
    db.session.commit()
    return jsonify({'message': 'Historial registrado', 'historial_id': historial.historial_id}), 201

@historial_bp.route('/historial/<int:historial_id>', methods=['PUT'])
def actualizar_historial(historial_id):
    historial = HistorialReserva.query.get_or_404(historial_id)
    data = request.json
    historial.campo_modificado = data.get('campo_modificado', historial.campo_modificado)
    historial.valor_antiguo = data.get('valor_antiguo', historial.valor_antiguo)
    historial.valor_nuevo = data.get('valor_nuevo', historial.valor_nuevo)
    historial.usuario_modificador_id = data.get('usuario_modificador_id', historial.usuario_modificador_id)
    db.session.commit()
    return jsonify({'message': 'Historial de reserva actualizado'})

@historial_bp.route('/historial/<int:historial_id>', methods=['DELETE'])
def eliminar_historial(historial_id):
    historial = HistorialReserva.query.get_or_404(historial_id)
    db.session.delete(historial)
    db.session.commit()
    return jsonify({'message': 'Historial de reserva eliminado'})
