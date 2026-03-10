from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Venta, DetalleVenta, Libro, Cliente
from .extensions import db
from flask_login import current_user, login_required

ventas_bp = Blueprint("ventas", __name__)

# LISTAR VENTAS
@ventas_bp.route("/ventas")
@login_required
def listar_ventas():
    ventas = Venta.query.order_by(Venta.fecha_venta.desc()).all()
    return render_template("ventas.html", ventas=ventas)

# CREAR VENTA
@ventas_bp.route("/ventas/crear", methods=["GET", "POST"])
@login_required
def crear_venta():
    clientes = Cliente.query.all()
    libros = Libro.query.filter(Libro.stock > 0).all()
    if request.method == "POST":
        import json
        id_cliente = request.form.get("id_cliente")
        metodo_pago = request.form.get("metodo_pago", "efectivo")
        detalles_json = request.form.get("detalles_json")
        try:
            detalles = json.loads(detalles_json) if detalles_json else []
        except Exception:
            detalles = []
        if not detalles:
            flash("Debe agregar al menos un libro.", "danger")
            return render_template("crear_venta.html", clientes=clientes, libros=libros)
        total = sum(float(d['subtotal']) for d in detalles)
        nueva_venta = Venta(
            id_cliente=id_cliente,
            id_usuario=current_user.id_usuario,
            total=total,
            metodo_pago=metodo_pago
        )
        db.session.add(nueva_venta)
        db.session.flush()  # Para obtener el id_venta
        for d in detalles:
            libro = Libro.query.get(int(d['id_libro']))
            if not libro or int(d['cantidad']) > libro.stock:
                flash(f"No hay suficiente stock para {d['titulo']}", "danger")
                db.session.rollback()
                return render_template("crear_venta.html", clientes=clientes, libros=libros)
            detalle = DetalleVenta(
                id_venta=nueva_venta.id_venta,
                id_libro=libro.id_libro,
                cantidad=int(d['cantidad']),
                precio_unitario=libro.precio,
                subtotal=float(d['subtotal'])
            )
            libro.stock -= int(d['cantidad'])
            db.session.add(detalle)
        db.session.commit()
        flash("Venta registrada exitosamente.", "success")
        return redirect(url_for("ventas.listar_ventas"))
    return render_template("crear_venta.html", clientes=clientes, libros=libros)

# DETALLE DE VENTA
@ventas_bp.route("/ventas/<int:id_venta>")
@login_required
def detalle_venta(id_venta):
    venta = Venta.query.get_or_404(id_venta)
    return render_template("detalle_venta.html", venta=venta)
