from flask import render_template

def list(historial):
    return render_template('historial/index.html', historial=historial)

def create():
    return render_template('historial/create.html')

def edit(historial_item):
    return render_template('historial/edit.html', historial=historial_item)
