from flask import render_template

def list(clientes):
    # Aquí deberías tener un archivo HTML llamado 'clientes/list.html'
    return render_template('clientes/index.html', clientes=clientes)

def create():
    # Aquí deberías tener un archivo HTML llamado 'clientes/create.html'
    return render_template('clientes/create.html')

def edit(cliente):
    # Aquí deberías tener un archivo HTML llamado 'clientes/edit.html'
    return render_template('clientes/edit.html', cliente=cliente)