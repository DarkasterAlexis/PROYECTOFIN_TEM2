from flask import Blueprint, request, redirect, url_for
from models.HorariosTrabajoPersonal_model import HorariosTrabajoPersonal
from views import HorariosTrabajoPersonal_view

horarios_bp = Blueprint('horarios', __name__, url_prefix="/horarios")

@horarios_bp.route("/")
def index():
    horarios = HorariosTrabajoPersonal.get_all()
    return HorariosTrabajoPersonal_view.list(horarios)

@horarios_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        Fecha = request.form['Fecha']
        HoraEntrada = request.form['HoraEntrada']
        HoraSalida = request.form['HoraSalida']
        DiaSemana = request.form['DiaSemana']

        horario = HorariosTrabajoPersonal(id, Fecha, HoraEntrada, HoraSalida, DiaSemana)
        horario.save()
        return redirect(url_for('horarios.index'))
    return HorariosTrabajoPersonal_view.create()

@horarios_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    horario = HorariosTrabajoPersonal.get_by_id(id)
    if request.method == 'POST':
        Fecha = request.form['Fecha']
        HoraEntrada = request.form['HoraEntrada']
        HoraSalida = request.form['HoraSalida']
        DiaSemana = request.form['DiaSemana']

        horario.update(Fecha=Fecha, HoraEntrada=HoraEntrada, HoraSalida=HoraSalida, DiaSemana=DiaSemana)
        return redirect(url_for('horarios.index'))
    return HorariosTrabajoPersonal_view.edit(horario)

@horarios_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    horario = HorariosTrabajoPersonal.get_by_id(id)
    horario.delete()
    return redirect(url_for('horarios.index'))
