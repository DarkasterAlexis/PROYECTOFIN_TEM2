from flask import request, redirect, url_for, Blueprint
from datetime import datetime, date, time # Importar para manejar fechas y horas desde los formularios

# Se importa la clase HorarioDisponible del modelo
from models.horariosDisponibles_model import HorarioDisponible
# Se asume que existe un módulo views/horarios_disponibles_view.py para renderizar las plantillas
from views import horarios_disponibles_view

# Se crea un Blueprint para organizar las rutas relacionadas con los horarios disponibles
# El prefijo de URL será /horarios-disponibles
horario_disponible_bp = Blueprint('horario_disponible', __name__, url_prefix="/horarios-disponibles")

@horario_disponible_bp.route("/")
def index():
    """
    Ruta para mostrar todos los horarios disponibles.
    Recupera todos los registros de horarios disponibles de la base de datos
    y los pasa a la vista para su visualización.
    """
    horarios_disponibles = HorarioDisponible.get_all()
    # Se llama a la función list del módulo horarios_disponibles_view para renderizar la lista
    return horarios_disponibles_view.list(horarios_disponibles)

@horario_disponible_bp.route("/create", methods=['GET', 'POST'])
def create():
    """
    Ruta para crear un nuevo registro de horario disponible.
    Si la solicitud es POST, recupera los datos del formulario,
    crea un nuevo objeto HorarioDisponible, lo guarda en la base de datos
    y redirige a la página de índice.
    Si la solicitud es GET, simplemente muestra el formulario de creación.
    """
    if request.method == 'POST':
        # Se recuperan los datos del formulario enviado
        recurso_id = request.form['recurso_id']
        fecha_str = request.form['fecha']
        hora_inicio_str = request.form['hora_inicio']
        hora_fin_str = request.form['hora_fin']
        # 'EstaDisponible' es un checkbox, su valor es 'on' si está marcado, si no, no se envía
        esta_disponible = 'esta_disponible' in request.form 
        notas = request.form.get('notas')

        try:
            # Se convierten las cadenas de fecha y hora a objetos date y time
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            hora_inicio_obj = datetime.strptime(hora_inicio_str, '%H:%M').time()
            hora_fin_obj = datetime.strptime(hora_fin_str, '%H:%M').time()

            # Se crea una nueva instancia del modelo HorarioDisponible
            horario = HorarioDisponible(
                RecursoID=recurso_id,
                Fecha=fecha_obj,
                HoraInicio=hora_inicio_obj,
                HoraFin=hora_fin_obj,
                EstaDisponible=esta_disponible,
                Notas=notas
            )
            # Se guarda el nuevo horario en la base de datos
            horario.save()
            # Se redirige a la ruta de índice de horarios disponibles
            return redirect(url_for('horario_disponible.index'))
        except ValueError as e:
            # Manejo de errores si el formato de fecha/hora es incorrecto
            # Podrías mostrar un mensaje de error al usuario en la vista de creación
            print(f"Error al parsear fecha/hora: {e}")
            return horarios_disponibles_view.create(error=str(e), form_data=request.form)


    # Si es una solicitud GET, se renderiza el formulario de creación
    return horarios_disponibles_view.create()

@horario_disponible_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    """
    Ruta para editar un registro de horario disponible existente.
    Recupera un horario disponible por su ID.
    Si la solicitud es POST, actualiza los datos del horario con los
    valores del formulario y lo guarda en la base de datos.
    Si la solicitud es GET, muestra el formulario de edición con los
    datos actuales del horario.
    """
    # Se recupera el horario a editar por su ID
    horario = HorarioDisponible.get_by_id(id)

    # Si el horario no existe, se puede manejar con un error 404 o redirigir
    if not horario:
        # Por simplicidad, redirigimos al índice si el horario no se encuentra
        return redirect(url_for('horario_disponible.index')) 

    if request.method == 'POST':
        # Se recuperan los datos actualizados del formulario
        recurso_id = request.form['recurso_id']
        fecha_str = request.form['fecha']
        hora_inicio_str = request.form['hora_inicio']
        hora_fin_str = request.form['hora_fin']
        esta_disponible = 'esta_disponible' in request.form
        notas = request.form.get('notas')

        try:
            # Se convierten las cadenas de fecha y hora a objetos date y time
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            hora_inicio_obj = datetime.strptime(hora_inicio_str, '%H:%M').time()
            hora_fin_obj = datetime.strptime(hora_fin_str, '%H:%M').time()

            # Se actualizan los atributos del objeto horario
            horario.update(
                RecursoID=recurso_id,
                Fecha=fecha_obj,
                HoraInicio=hora_inicio_obj,
                HoraFin=hora_fin_obj,
                EstaDisponible=esta_disponible,
                Notas=notas
            )
            
            # Se redirige a la ruta de índice de horarios disponibles
            return redirect(url_for('horario_disponible.index'))
        except ValueError as e:
            # Manejo de errores si el formato de fecha/hora es incorrecto
            print(f"Error al parsear fecha/hora: {e}")
            return horarios_disponibles_view.edit(horario, error=str(e), form_data=request.form)


    # Si es una solicitud GET, se renderiza el formulario de edición con los datos del horario
    return horarios_disponibles_view.edit(horario)

@horario_disponible_bp.route("/delete/<int:id>")
def delete(id):
    """
    Ruta para eliminar un registro de horario disponible.
    Recupera un horario disponible por su ID y lo elimina de la base de datos.
    Luego redirige a la página de índice de horarios disponibles.
    """
    # Se recupera el horario a eliminar por su ID
    horario = HorarioDisponible.get_by_id(id)

    # Se verifica si el horario existe antes de intentar eliminarlo
    if horario:
        horario.delete()
    
    # Se redirige a la ruta de índice de horarios disponibles
    return redirect(url_for('horario_disponible.index'))

