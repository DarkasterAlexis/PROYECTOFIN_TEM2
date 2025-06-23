from flask import render_template

def list(recursos):
    return render_template('recursos/list.html', recursos=recursos)

def create():
    return render_template('recursos/create.html')

def edit(recurso):
    return render_template('recursos/edit.html', recurso=recurso)