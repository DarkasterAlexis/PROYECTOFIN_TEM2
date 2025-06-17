from flask import render_template

def list(configuraciones):
    return render_template('configNeg/index.html', configuraciones=configuraciones)

def create():
    return render_template('configNeg/create.html')

def edit(configuracion):
    return render_template('configNeg/edit.html', configuracion=configuracion)
