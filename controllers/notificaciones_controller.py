from flask import Blueprint, request, redirect,url_for
from models.notificaciones_model import Notificacion
from views import notificaciones_view

notificaciones_bp = Blueprint('notificacion', __name__,url_prefix="/notificaciones")

@notificaciones_bp.route("/")
def index():
    notificacion = Notificacion.get_all()
    return notificaciones_view.list(notificacion)


@notificaciones_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    notifi = Notificacion.get_by_id(id)
    notifi.delete()
    return redirect(url_for('notificacion.index'))
