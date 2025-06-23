from flask import request, redirect, url_for, Blueprint

# Se importa la clase Recurso del modelo
from models.recursos_model import Recurso
# Se asume que existe un módulo views/recurso_view.py para renderizar las plantillas
from views import recurso_view

# Se crea un Blueprint para organizar las rutas relacionadas con los recursos
# El prefijo de URL será /recursos
recurso_bp = Blueprint('recurso', __name__, url_prefix="/recursos")

@recurso_bp.route("/")
def index():
    """
    Ruta para mostrar todos los recursos.
    Recupera todos los registros de recursos de la base de datos
    y los pasa a la vista para su visualización.
    """
    recursos = Recurso.get_all()
    # Se llama a la función list del módulo recurso_view para renderizar la lista
    return recurso_view.list(recursos)

@recurso_bp.route("/create", methods=['GET', 'POST'])
def create():
    """
    Ruta para crear un nuevo registro de recurso.
    Si la solicitud es POST, recupera los datos del formulario,
    crea un nuevo objeto Recurso, lo guarda en la base de datos
    y redirige a la página de índice.
    Si la solicitud es GET, simplemente muestra el formulario de creación.
    """
    if request.method == 'POST':
        # Se recuperan los datos del formulario enviado
        nombre_recurso = request.form['nombre_recurso']
        tipo_recurso = request.form['tipo_recurso']
        capacidad = int(request.form['capacidad']) # Convertir a entero
        descripcion = request.form.get('descripcion') # Opcional

        # Se crea una nueva instancia del modelo Recurso
        recurso = Recurso(
            NombreRecurso=nombre_recurso,
            TipoRecurso=tipo_recurso,
            Capacidad=capacidad,
            Descripcion=descripcion
        )
        # Se guarda el nuevo recurso en la base de datos
        recurso.save()
        # Se redirige a la ruta de índice de recursos
        return redirect(url_for('recurso.index'))

    # Si es una solicitud GET, se renderiza el formulario de creación
    return recurso_view.create()

@recurso_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    """
    Ruta para editar un registro de recurso existente.
    Recupera un recurso por su ID.
    Si la solicitud es POST, actualiza los datos del recurso con los
    valores del formulario y lo guarda en la base de datos.
    Si la solicitud es GET, muestra el formulario de edición con los
    datos actuales del recurso.
    """
    # Se recupera el recurso a editar por su ID
    recurso = Recurso.get_by_id(id)

    # Si el recurso no existe, se puede manejar con un error 404 o redirigir
    if not recurso:
        # Por simplicidad, redirigimos al índice si el recurso no se encuentra
        return redirect(url_for('recurso.index')) 

    if request.method == 'POST':
        # Se recuperan los datos actualizados del formulario
        nombre_recurso = request.form['nombre_recurso']
        tipo_recurso = request.form['tipo_recurso']
        capacidad = int(request.form['capacidad']) # Convertir a entero
        descripcion = request.form.get('descripcion') # Opcional

        # Se actualizan los atributos del objeto recurso
        recurso.update(
            NombreRecurso=nombre_recurso,
            TipoRecurso=tipo_recurso,
            Capacidad=capacidad,
            Descripcion=descripcion
        )
        
        # Se redirige a la ruta de índice de recursos
        return redirect(url_for('recurso.index'))

    # Si es una solicitud GET, se renderiza el formulario de edición con los datos del recurso
    return recurso_view.edit(recurso)

@recurso_bp.route("/delete/<int:id>")
def delete(id):
    """
    Ruta para eliminar un registro de recurso.
    Recupera un recurso por su ID y lo elimina de la base de datos.
    Luego redirige a la página de índice de recursos.
    """
    # Se recupera el recurso a eliminar por su ID
    recurso = Recurso.get_by_id(id)

    # Se verifica si el recurso existe antes de intentar eliminarlo
    if recurso:
        recurso.delete()
    
    # Se redirige a la ruta de índice de recursos
    return redirect(url_for('recurso.index'))

