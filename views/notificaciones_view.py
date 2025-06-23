from flask import render_template

def list(notificaciones):
    return render_template('notificaciones/index.html', notificaciones=notificaciones)
