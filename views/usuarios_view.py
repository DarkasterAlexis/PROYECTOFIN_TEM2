from flask import render_template

def list(usuarios):
    return render_template('usuarios/index.html', usuarios=usuarios)
