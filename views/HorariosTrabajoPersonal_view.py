from flask import render_template

def list(horarios):
    return render_template('horarios/index.html', horarios=horarios)

def create():
    return render_template('horarios/create.html')

def edit(horario):
    return render_template('horarios/edit.html', horario=horario)
