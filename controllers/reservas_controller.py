from flask import Blueprint, request, redirect, url_for
from models.reservas_model import Reserva
from views import reserva_view

reserva_bp = Blueprint('reserva', __name__, url_prefix="/reserva")

@reserva_bp.route("/")
def index():
    reservas = Reserva.get_all()
    return reserva_view.list(reservas)

@reserva_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        ClienteID = request.form['ClienteID']
        RecursoID = request.form['RecursoID']
        FechaReserva = request.form['FechaReserva']
        HoraInicio = request.form['HoraInicio']
        HoraFin = request.form['HoraFin']
        NumeroPersonas = request.form.get('NumeroPersonas')
        TipoCita = request.form.get('TipoCita')
        EstadoReserva = request.form.get('EstadoReserva')
        FechaCreacion = request.form.get('FechaCreacion')
        NotasCliente = request.form.get('NotasCliente')

        reserva = Reserva(ClienteID, RecursoID, FechaReserva, HoraInicio, HoraFin,
                          NumeroPersonas, TipoCita, EstadoReserva, FechaCreacion, NotasCliente)
        reserva.save()
        return redirect(url_for('reserva.index'))
    return reserva_view.create()

@reserva_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    reserva = Reserva.get_by_id(id)
    if request.method == 'POST':
        ClienteID = request.form['ClienteID']
        RecursoID = request.form['RecursoID']
        FechaReserva = request.form['FechaReserva']
        HoraInicio = request.form['HoraInicio']
        HoraFin = request.form['HoraFin']
        NumeroPersonas = request.form.get('NumeroPersonas')
        TipoCita = request.form.get('TipoCita')
        EstadoReserva = request.form.get('EstadoReserva')
        FechaCreacion = request.form.get('FechaCreacion')
        NotasCliente = request.form.get('NotasCliente')

        reserva.update(ClienteID=ClienteID, RecursoID=RecursoID, FechaReserva=FechaReserva, HoraInicio=HoraInicio,
                       HoraFin=HoraFin, NumeroPersonas=NumeroPersonas, TipoCita=TipoCita,
                       EstadoReserva=EstadoReserva, FechaCreacion=FechaCreacion, NotasCliente=NotasCliente)
        return redirect(url_for('reserva.index'))
    return reserva_view.edit(reserva)

@reserva_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    reserva = Reserva.get_by_id(id)
    reserva.delete()
    return redirect(url_for('reserva.index'))
