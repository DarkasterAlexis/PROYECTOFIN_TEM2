from flask import Blueprint, request, redirect,url_for
from models.configuracionNeg_model import ConfiguracionNegocio
from views import configuracionNeg_view

configuracion_bp = Blueprint('configuracion', __name__,url_prefix="/configNeg")

@configuracion_bp.route("/")
def index():
    configNeg = ConfiguracionNegocio.get_all()
    return configuracionNeg_view.list(configNeg)

@configuracion_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombreparametro=request.form['nombreparametro']
        valorparametro=request.form['valorparametro']
        config = ConfiguracionNegocio(nombreparametro,valorparametro)
        config.save()
        return redirect(url_for('configuracion.index'))
    return configuracionNeg_view.create()

@configuracion_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    config = ConfiguracionNegocio.get_by_id(id)    
    if request.method == 'POST':
        nombreparametro=request.form['nombre_parametro']
        valorparametro=request.form['valor_parametro']
        config.update(nombreparametro=nombreparametro,valorparametro=valorparametro)
        return redirect(url_for('configuracion.index'))
    return configuracionNeg_view.edit(config)

@configuracion_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    config = ConfiguracionNegocio.get_by_id(id)
    config.delete()
    return redirect(url_for('configuracion.index'))