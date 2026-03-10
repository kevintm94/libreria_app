from flask import Blueprint, render_template, request, redirect, url_for
from .models import Cliente
from .extensions import db

clientes_bp = Blueprint("clientes", __name__)

# LISTAR CLIENTES
@clientes_bp.route("/clientes")
def listar_clientes():
    # Tomamos el parámetro de búsqueda desde la URL
    busqueda = request.args.get("busqueda", "")

    if busqueda:
        # Filtramos por nombre, apellido o email
        clientes = Cliente.query.filter(
            (Cliente.nombre.ilike(f"%{busqueda}%")) |
            (Cliente.apellido.ilike(f"%{busqueda}%")) |
            (Cliente.email.ilike(f"%{busqueda}%"))
        ).all()
    else:
        clientes = Cliente.query.all()

    return render_template("clientes.html", clientes=clientes, busqueda=busqueda)


# CREAR CLIENTE
@clientes_bp.route("/clientes/crear", methods=["GET","POST"])
def crear_cliente():

    error = None

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]

        if not nombre:
            error = "El nombre es obligatorio"

        elif not apellido:
            error = "El apellido es obligatorio"

        elif not email:
            error = "El email es obligatorio"

        cliente_existente = Cliente.query.filter_by(email=email).first()

        if cliente_existente:
            error = "El email ya existe"

        if error:
            return render_template("crear_cliente.html", error=error)

        nuevo_cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=request.form.get("telefono", ""),
            direccion=request.form.get("direccion", "")
        )

        db.session.add(nuevo_cliente)
        db.session.commit()

        return redirect(url_for("clientes.listar_clientes"))

    return render_template("crear_cliente.html", error=error)

# EDITAR CLIENTE
@clientes_bp.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    error = None

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]

        # VALIDACIONES
        if not nombre:
            error = "El nombre es obligatorio"
        elif not apellido:
            error = "El apellido es obligatorio"
        elif not email:
            error = "El email es obligatorio"

        # Validar email duplicado (excepto el cliente actual)
        cliente_existente = Cliente.query.filter(Cliente.email==email, Cliente.id_cliente!=id).first()
        if cliente_existente:
            error = "El email ya existe"

        if error:
            return render_template("editar_cliente.html", cliente=cliente, error=error)

        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.telefono = request.form.get("telefono", "")
        cliente.direccion = request.form.get("direccion", "")

        db.session.commit()

        return redirect(url_for("clientes.listar_clientes"))

    return render_template("editar_cliente.html", cliente=cliente, error=error)

# ELIMINAR CLIENTE
@clientes_bp.route("/clientes/eliminar/<int:id>", methods=["POST"])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for("clientes.listar_clientes"))
