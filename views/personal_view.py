from flask import render_template

def list(personal):
    return render_template('personal/index.html', personal=personal)

def create():
    return render_template('personal/create.html')

def edit(persona):
    return render_template('personal/edit.html', personal=persona)
