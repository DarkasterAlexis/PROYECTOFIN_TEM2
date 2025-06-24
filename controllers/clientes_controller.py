from flask import request, redirect, url_for, Blueprint,flash
from models.clientes_model import Cliente
from models.usuarios_model import Usuario
from views import clientes_view
from werkzeug.security import generate_password_hash,check_password_hash

# Se crea un Blueprint para organizar las rutas relacionadas con los clientes
# El prefijo de URL será /clientes
cliente_bp = Blueprint('cliente', __name__, url_prefix="/clientes")

@cliente_bp.route("/")
def index():
    
    # Ruta para mostrar todos los clientes.
    # Recupera todos los registros de clientes de la base de datos
    # y los pasa a la vista para su visualización.
    
    clientes = Cliente.get_all()
    # Se llama a la función list del módulo cliente_view para renderizar la lista
    return clientes_view.list(clientes)

@cliente_bp.route("/create", methods=['GET', 'POST'])
def create():
    
    # Ruta para crear un nuevo registro de cliente.
    # Si la solicitud es POST, recupera los datos del formulario,
    # crea un nuevo objeto Cliente, lo guarda en la base de datos
    # y redirige a la página de índice de clientes.
    # Si la solicitud es GET, simplemente muestra el formulario de creación.
    
    if request.method == 'POST':
        # Se recuperan los datos del formulario enviado
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        rol = request.form['rol']    
        # ContraseñaHash es opcional, se recupera si está presente
        password = request.form.get('password') 
        # Se crea una nueva instancia del modelo Cliente
        cliente = Cliente(nombre, apellido, email,telefono,rol, password)
        # Se guarda el nuevo cliente en la base de datos
        cliente.save()
        usuario = Usuario(
            Nombre =nombre,
            Apellido = apellido,
            email = email,
            Telefono = telefono,
            password = generate_password_hash(password),
            idtipouser = cliente.id,
            tiprelacion = "cliente",
            rol = rol
        )
        usuario.save() 
        # Se redirige a la ruta de índice de clientes
        return redirect(url_for('cliente.index'))

    # Si es una solicitud GET, se renderiza el formulario de creación
    return clientes_view.create()

@cliente_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    
    # Ruta para editar un registro de cliente existente.
    # Recupera un cliente por su ID.
    # Si la solicitud es POST, actualiza los datos del cliente con los
    # valores del formulario y lo guarda en la base de datos.
    # Si la solicitud es GET, muestra el formulario de edición con los
    # datos actuales del cliente.
    
    # Se recupera el cliente a editar por su ID
    cliente = Cliente.get_by_id(id)

    # Si el cliente no existe, se puede manejar con un error 404 o redirigir
    if not cliente:
        # Por simplicidad, redirigimos al índice si el cliente no se encuentra
        return redirect(url_for('cliente.index')) 

    if request.method == 'POST':
        # Se recuperan los datos actualizados del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        rol = request.form['rol']
        password = request.form.get('password') # Opcional

        # Se actualizan los atributos del objeto cliente
        cliente.update(nombre=nombre, apellido=apellido, email=email,
                       telefono=telefono,rol=rol, password=generate_password_hash(password))
        
        # Se redirige a la ruta de índice de clientes
        return redirect(url_for('cliente.index'))

    # Si es una solicitud GET, se renderiza el formulario de edición con los datos del cliente
    return clientes_view.edit(cliente)

@cliente_bp.route("/delete/<int:id>")
def delete(id):
    
    # Ruta para eliminar un registro de cliente.
    # Recupera un cliente por su ID y lo elimina de la base de datos.
    # Luego redirige a la página de índice de clientes.
    
    # Se recupera el cliente a eliminar por su ID
    cliente = Cliente.get_by_id(id)

    # Se verifica si el cliente existe antes de intentar eliminarlo
    if cliente:
        cliente.delete()
    
    # Se redirige a la ruta de índice de clientes
    return redirect(url_for('cliente.index'))


