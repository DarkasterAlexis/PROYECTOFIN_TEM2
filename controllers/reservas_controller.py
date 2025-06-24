from flask import Blueprint, request, redirect, url_for
from models.reservas_model import Reserva
from models.historialcambres_model import HistorialCambioReserva
from views import reservas_view
from flask_login import current_user

reserva_bp = Blueprint('reserva', __name__, url_prefix="/reserva")

@reserva_bp.route("/")
def index():
    reservas = Reserva.get_all()
    return reservas_view.list(reservas)

@reserva_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        id = request.form['id']
        RecursoID = request.form['RecursoID']
        FechaReserva = request.form['FechaReserva']
        HoraInicio = request.form['HoraInicio']
        HoraFin = request.form['HoraFin']
        NumeroPersonas = request.form.get('NumeroPersonas')
        TipoCita = request.form.get('TipoCita')
        EstadoReserva = request.form.get('EstadoReserva')
        FechaCreacion = request.form.get('FechaCreacion')
        NotasCliente = request.form.get('NotasCliente')

        reserva = Reserva(id, RecursoID, FechaReserva, HoraInicio, HoraFin,
                          NumeroPersonas, TipoCita, EstadoReserva, FechaCreacion, NotasCliente)
        reserva.save()
        return redirect(url_for('reserva.index'))
    return reservas_view.create()

@reserva_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    reserva = Reserva.get_by_id(id)
    if request.method == 'POST':
        cambios= []
        campos_for={
            "id" : request.form['id'],
            "RecursoID" : request.form['RecursoID'],
            "FechaReserva" : request.form['FechaReserva'],
            "HoraInicio" : request.form['HoraInicio'],
            "HoraFin" : request.form['HoraFin'],
            "NumeroPersonas" : request.form.get('NumeroPersonas'),
            "TipoCita" : request.form.get('TipoCita'),
            "EstadoReserva" : request.form.get('EstadoReserva'),
            "FechaCreacion" : request.form.get('FechaCreacion'),
            "NotasCliente" : request.form.get('NotasCliente'),
        }
        for campo, valor_nuevo in campos_for.items():
            valor_anterior= getattr(reserva,campo)
            if str(valor_anterior)!= str(valor_nuevo):
                cambios.append(HistorialCambioReserva(
                reser_id=id,
                campomodificado=campo,
                valorantiguo=str(valor_anterior),
                valornuevo=str(valor_nuevo),
                iomodifi_id=current_user.id
                ))
        reserva.save()
        return redirect(url_for('reserva.index'))
    return reservas_view.edit(reserva)

@reserva_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    reserva = Reserva.get_by_id(id)
    reserva.delete()
    return redirect(url_for('reserva.index'))
