from flask import render_template

def list(horarios_disponibles):
    return render_template('horarios_disponibles/list.html', horarios_disponibles=horarios_disponibles)

def create(error=None, form_data=None):
    return render_template('horarios_disponibles/create.html', error=error, form_data=form_data)

def edit(horario, error=None, form_data=None):
    return render_template('horarios_disponibles/edit.html', horario=horario, error=error, form_data=form_data)