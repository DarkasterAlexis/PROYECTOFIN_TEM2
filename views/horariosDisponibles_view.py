from flask import render_template

def list(horarios_disponibles):
    return render_template('horariosDisponibles/index.html', horarios_disponibles=horarios_disponibles)

def create(error=None, form_data=None):
    return render_template('horariosDisponibles/create.html', error=error, form_data=form_data)

def edit(horario, error=None, form_data=None):
    return render_template('horariosDisponibles/edit.html', horario=horario, error=error, form_data=form_data)