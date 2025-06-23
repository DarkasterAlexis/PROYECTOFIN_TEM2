from flask import Blueprint, request, redirect, url_for
from models.historialcambres_model import HistorialCambioReserva
from views import historialcambres_view

historial_bp = Blueprint('historial', __name__,url_prefix="/historial")

@historial_bp.route("/")
def index():
    historia = HistorialCambioReserva.get_all()
    return historialcambres_view.list(historia)


@historial_bp.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    historial = HistorialCambioReserva.get_by_id(id)
    historial.delete()
    return redirect(url_for('historial.index'))
