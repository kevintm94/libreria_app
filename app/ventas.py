from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app
from .models import Venta, DetalleVenta, Libro, Cliente
from .extensions import db, get_groq_client
from flask_login import current_user, login_required
from sqlalchemy import func
from datetime import datetime, timedelta
import json

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

@ventas_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard con datos dinámicos desde la base de datos."""

    if current_user.rol not in ['admin', 'gerente']:
        flash('No tienes permiso para acceder al dashboard', 'danger')
        return redirect(url_for('ventas.listar_ventas'))

    # --- 1. CÁLCULO DE KPIs ---
    today = datetime.utcnow().date()
    seven_days_ago = today - timedelta(days=6)
    start_of_month = today.replace(day=1)

    # KPIs de ventas
    ventas_hoy = db.session.query(func.sum(Venta.total)).filter(func.date(Venta.fecha_venta) == today).scalar() or 0
    ventas_semana_kpi = db.session.query(func.sum(Venta.total)).filter(Venta.fecha_venta >= seven_days_ago).scalar() or 0
    ventas_mes_kpi = db.session.query(func.sum(Venta.total)).filter(Venta.fecha_venta >= start_of_month).scalar() or 0

    # KPIs de inventario y clientes
    libros_vendidos_mes = db.session.query(func.sum(DetalleVenta.cantidad)).join(Venta).filter(Venta.fecha_venta >= start_of_month).scalar() or 0
    stock_total = db.session.query(func.sum(Libro.stock)).scalar() or 0

    # Clientes nuevos este mes (aquellos cuya primera compra fue este mes)
    subquery = db.session.query(
        Venta.id_cliente,
        func.min(Venta.fecha_venta).label('primera_compra')
    ).group_by(Venta.id_cliente).subquery()
    clientes_nuevos_mes = db.session.query(func.count(subquery.c.id_cliente)).filter(subquery.c.primera_compra >= start_of_month).scalar() or 0

    kpis = {
        'ventas_hoy': ventas_hoy,
        'ventas_semana': ventas_semana_kpi,
        'ventas_mes': ventas_mes_kpi,
        'libros_vendidos': libros_vendidos_mes,
        'stock_total': stock_total,
        'clientes_nuevos': clientes_nuevos_mes
    }

    # --- 2. DATOS PARA GRÁFICA DE VENTAS SEMANALES ---
    fechas_semana = [today - timedelta(days=i) for i in range(6, -1, -1)]
    dias_es = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    dias_labels = [dias_es[d.weekday()] for d in fechas_semana]

    ventas_por_dia_query = db.session.query(
        func.date(Venta.fecha_venta).label('dia'),
        func.sum(Venta.total).label('total')
    ).filter(Venta.fecha_venta >= seven_days_ago).group_by('dia').all()

    ventas_dict = {v.dia: float(v.total) for v in ventas_por_dia_query}
    ventas_semana_data = [ventas_dict.get(d, 0) for d in fechas_semana]

    # --- 3. DATOS PARA GRÁFICA DE STOCK POR GÉNERO ---
    stock_por_genero_query = db.session.query(
        Libro.genero,
        func.sum(Libro.stock).label('total_stock')
    ).group_by(Libro.genero).order_by(func.sum(Libro.stock).desc()).limit(7).all()

    generos_data = [g.genero or 'Sin Género' for g in stock_por_genero_query]
    stock_generos_data = [int(g.total_stock) for g in stock_por_genero_query]

    # --- 4. DATOS PARA TABLA DE TOP 5 LIBROS MÁS VENDIDOS ---
    top_libros_query = db.session.query(
        Libro.titulo,
        Libro.stock,
        func.sum(DetalleVenta.cantidad).label('ventas')
    ).join(DetalleVenta, DetalleVenta.id_libro == Libro.id_libro)\
     .group_by(Libro.id_libro)\
     .order_by(func.sum(DetalleVenta.cantidad).desc())\
     .limit(5).all()

    top_libros_data = [
        {'titulo': libro.titulo, 'ventas': int(libro.ventas), 'stock': libro.stock}
        for libro in top_libros_query
    ]

    return render_template('dashboard.html',
                          dias_semana=dias_labels,
                          ventas_semana=ventas_semana_data,
                          generos=generos_data,
                          stock_generos=stock_generos_data,
                          kpis=kpis,
                          top_libros=top_libros_data)

@ventas_bp.route('/dashboard/analisis_ia', methods=['POST'])
@login_required
def analisis_ia():
    """Endpoint para generar análisis con IA."""
    if current_user.rol not in ['admin', 'gerente']:
        return jsonify({'error': 'No tienes permiso para esta acción'}), 403

    task = request.json.get('task')
    if not task:
        return jsonify({'error': 'No se especificó la tarea'}), 400

    groq_client = get_groq_client()
    if not groq_client:
        return jsonify({'error': 'El cliente de IA no está configurado'}), 500

    # Tarea 1: Analizar ventas del último mes (Implementación de ejemplo)
    if task == 'ventas_mes':
        try:
            # 1. Obtener datos de la base de datos
            treinta_dias_atras = datetime.utcnow() - timedelta(days=30)
            ventas = db.session.query(
                func.date(Venta.fecha_venta).label('dia'),
                func.sum(Venta.total).label('total_dia')
            ).filter(Venta.fecha_venta >= treinta_dias_atras).group_by('dia').order_by('dia').all()

            if not ventas:
                return jsonify({'error': 'No hay datos de ventas en los últimos 30 días para analizar.'}), 404

            # 2. Formatear datos y construir el prompt para la IA, inyectando los datos del gráfico.
            data_str = "\n".join([f"Día: {v.dia}, Total Ventas: {v.total_dia:.2f}" for v in ventas])
            labels_json = json.dumps([str(v.dia) for v in ventas])
            values_json = json.dumps([float(v.total_dia) for v in ventas])

            prompt = f"""
            Eres un analista de datos experto para una librería. Analiza los siguientes datos de ventas de los últimos 30 días.
            Proporciona un resumen conciso y valioso en formato de texto.
            
            Datos de ventas:
            {data_str}
            
            Tu respuesta DEBE ser un objeto JSON válido con la siguiente estructura. Rellena únicamente el campo `analysis_text`.
            {{
              "analysis_text": "Un análisis en formato de texto de 2 o 3 párrafos sobre las tendencias, picos, y posibles conclusiones. Usa markdown para formato (ej: **negritas**, - listas).",
              "chart_data": {{
                "chart_type": "line",
                "label": "Ventas Diarias",
                "labels": {labels_json},
                "values": {values_json}
              }}
            }}
            """
            return consultar_groq(groq_client, prompt, current_app.config['GROQ_MODEL'])

        except Exception as e:
            return jsonify({'error': f'Error al procesar el análisis: {str(e)}'}), 500

    elif task == 'perfil_cliente':
            try:
                # Consultar top 5 clientes por monto total comprado
                clientes = db.session.query(
                    Cliente.nombre, Cliente.apellido, func.sum(Venta.total).label('total_comprado')
                ).join(Venta).group_by(Cliente.id_cliente).order_by(func.sum(Venta.total).desc()).limit(5).all()
                
                if not clientes:
                    return jsonify({'error': 'No hay suficientes datos de ventas.'}), 404

                # Formatear datos y construir el prompt para la IA
                data_str = "\n".join([f"- {c.nombre} {c.apellido}: ${c.total_comprado}" for c in clientes])
                labels_json = json.dumps([f"{c.nombre} {c.apellido}" for c in clientes])
                values_json = json.dumps([float(c.total_comprado) for c in clientes])
                
                prompt = f"""
                Analiza a los mejores clientes de la librería. Define brevemente su perfil (basado en su gasto) y sugiere 2 acciones de fidelización.
                
                Top Clientes:
                {data_str}
                
                Tu respuesta DEBE ser un JSON válido. Rellena únicamente el campo analysis_text.
                {{
                "analysis_text": "Perfil y estrategias en markdown.",
                "chart_data": {{
                    "chart_type": "doughnut", 
                    "label": "Gasto Total",
                    "labels": {labels_json},
                    "values": {values_json}
                }}
                }}
                """
                return consultar_groq(groq_client, prompt, current_app.config['GROQ_MODEL'])
            except Exception as e:
                return jsonify({'error': f'Error en perfil cliente: {str(e)}'}), 500
    
    return jsonify({'error': 'Tarea no reconocida'}), 400

def consultar_groq(client, prompt, model):
    """Función auxiliar para llamar a Groq y manejar la respuesta JSON"""
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        temperature=0.3,
        max_tokens=1024,
        response_format={"type": "json_object"},
    )
    return jsonify(json.loads(completion.choices[0].message.content))