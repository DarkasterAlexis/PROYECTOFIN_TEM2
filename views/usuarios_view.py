from flask import render_template

def list(usuarios):
    return render_template('usuarios/index.html', usuarios=usuarios)

def login(next=None):
    return render_template("login/login.html",next=next)

def dashboard(usuario):
    return render_template("inicioclient/index.html",usuario=usuario)

def inicioperson(usuario):
    return render_template("personal/index.html",usuario=usuario)

def inicioadmin(usuario):
    return render_template("inicioadministrador/index.html",usuario=usuario)
