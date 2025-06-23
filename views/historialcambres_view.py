from flask import render_template

def list(historial):
    return render_template('historial/index.html', historial=historial)

