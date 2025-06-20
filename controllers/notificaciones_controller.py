from flask import Blueprint, request, redirect,url_for
from models.notificaciones_model import Notificacion
from views import notificaciones_view

notificaciones_bp = Blueprint('notificacion', __name__,url_prefix="/notificaciones")

@notificaciones_bp.route("/")
def index():
    servicios = Notificacion.get_all()
    return notificaciones_view.list(servicios)

@notificaciones_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        tiponotificacion=request.form['tipo_notificacion']
        mensaje=request.form['mensaje']
        fechaenvio = request.form['fechaenvio']
        estadoenvio=request.form['estadoenvio']
        notifi = Notificacion(tiponotificacion,mensaje,fechaenvio,estadoenvio)
        notifi.save()
        return redirect(url_for('notificacion.index'))
    return notificaciones_view.create()

@notificaciones_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    notifi = Notificacion.get_by_id(id)
    if request.method == 'POST':
        tiponotificacion=request.form['tipo_notificacion']
        mensaje=request.form['mensaje']
        fechaenvio = request.form['fechaenvio']
        estadoenvio=request.form['estadoenvio']
        notifi.update(tiponotificacion=tiponotificacion,mensaje=mensaje,fechaenvio=fechaenvio,estadoenvio=estadoenvio)
        return redirect(url_for('notificacion.index'))
    return notificaciones_view.edit()

@notificaciones_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    notifi = Notificacion.get_by_id(id)
    notifi.delete()
    return redirect(url_for('notificacion.index'))
