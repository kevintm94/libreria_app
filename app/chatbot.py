from flask import Blueprint, render_template, request, jsonify, current_app
from flask_login import login_required, current_user
from app.extensions import db, get_groq_client
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import json
import logging
import re

# Crear blueprint
chatbot_bp = Blueprint('chatbot', __name__, url_prefix='/chatbot')
logger = logging.getLogger(__name__)

# ============================================
# CONTEXTO DE LA BASE DE DATOS
# ============================================
DB_SCHEMA_CONTEXT = """
Eres un experto en SQL para MySQL. Convierte las preguntas en español a consultas SQL precisas para una librería.

== TABLAS DISPONIBLES ==

1. libro: 
   - id_libro (INT, PRIMARY KEY, AUTO_INCREMENT)
   - isbn (VARCHAR(20), UNIQUE)
   - titulo (VARCHAR(200), NOT NULL)
   - autor (VARCHAR(100), NOT NULL)
   - editorial (VARCHAR(100))
   - anio_publicacion (INT)
   - genero (VARCHAR(50))
   - precio (DECIMAL(10,2), NOT NULL)
   - stock (INT, DEFAULT 0)
   - descripcion (TEXT)
   - paginas (INT)
   - idioma (VARCHAR(30), DEFAULT 'Español')

2. cliente:
   - id_cliente (INT, PRIMARY KEY, AUTO_INCREMENT)
   - nombre (VARCHAR(100), NOT NULL)
   - apellido (VARCHAR(100), NOT NULL)
   - email (VARCHAR(100), UNIQUE)
   - telefono (VARCHAR(20))
   - direccion (TEXT)

3. venta:
   - id_venta (INT, PRIMARY KEY, AUTO_INCREMENT)
   - id_cliente (INT, FOREIGN KEY)
   - id_usuario (INT, FOREIGN KEY)
   - fecha_venta (DATETIME, DEFAULT CURRENT_TIMESTAMP)
   - total (DECIMAL(10,2), NOT NULL)
   - metodo_pago (ENUM('efectivo', 'tarjeta', 'transferencia', 'otros'))

4. detalle_venta:
   - id_detalle (INT, PRIMARY KEY, AUTO_INCREMENT)
   - id_venta (INT, FOREIGN KEY)
   - id_libro (INT, FOREIGN KEY)
   - cantidad (INT, NOT NULL)
   - precio_unitario (DECIMAL(10,2), NOT NULL)
   - subtotal (DECIMAL(10,2), NOT NULL)

5. usuario:
   - id_usuario (INT, PRIMARY KEY, AUTO_INCREMENT)
   - usuario (VARCHAR(50), UNIQUE)
   - password (VARCHAR(250))
   - email (VARCHAR(100), UNIQUE)
   - nombre_completo (VARCHAR(100))
   - rol (VARCHAR(20): 'admin', 'gerente', 'vendedor')

== EJEMPLOS DE CONSULTAS (MySQL) ==

Pregunta: "libros de García Márquez"
SQL: SELECT * FROM libro WHERE autor LIKE '%García Márquez%';

Pregunta: "libros con stock menor a 5"
SQL: SELECT titulo, stock FROM libro WHERE stock < 5 ORDER BY stock ASC;

Pregunta: "ventas de la semana pasada"
SQL: SELECT v.id_venta, c.nombre, c.apellido, v.fecha_venta, v.total 
     FROM venta v JOIN cliente c ON v.id_cliente = c.id_cliente 
     WHERE v.fecha_venta >= CURDATE() - INTERVAL 7 DAY 
     ORDER BY v.fecha_venta DESC;

Pregunta: "total de ventas por mes"
SQL: SELECT DATE_FORMAT(fecha_venta, '%Y-%m') as mes, 
            COUNT(*) as num_ventas, 
            SUM(total) as total_ventas 
     FROM venta 
     GROUP BY mes 
     ORDER BY mes DESC;

== INSTRUCCIONES ==
- Usa sintaxis válida para MySQL
- Responde SOLO con la consulta SQL, sin explicaciones
- Usa LIMIT para limitar resultados (máximo 50)
- Siempre incluye ORDER BY para resultados ordenados
"""

# ============================================
# FUNCIÓN PARA EJECUTAR SQL CON SQLALCHEMY
# ============================================

def execute_sql_query(sql_query):
    """
    Ejecuta una consulta SQL usando SQLAlchemy.
    Solo permite consultas SELECT por seguridad.
    """
    # Limpiar la consulta
    sql_clean = sql_query.replace('```sql', '').replace('```', '').strip()
    
    # Validar que solo sea SELECT
    if not re.match(r'^\s*SELECT\s+', sql_clean, re.IGNORECASE):
        return {"error": "Solo se permiten consultas SELECT por seguridad"}
    
    try:
        # Ejecutar consulta usando SQLAlchemy
        result = db.session.execute(text(sql_clean))
        
        # Convertir resultados a lista de diccionarios
        rows = []
        for row in result:
            # row._mapping es un diccionario con los nombres de columna
            row_dict = {}
            for key in row._mapping.keys():
                value = row._mapping[key]
                # Convertir tipos no serializables (datetime, decimal)
                if hasattr(value, 'isoformat'):  # Para fechas
                    value = value.isoformat()
                elif hasattr(value, '__float__'):  # Para Decimal
                    value = float(value)
                elif not isinstance(value, (str, int, float, bool, type(None))):
                    value = str(value)
                row_dict[key] = value
            rows.append(row_dict)
        
        return {"success": True, "data": rows, "count": len(rows)}
        
    except SQLAlchemyError as e:
        logger.error(f"Error SQLAlchemy: {e}")
        return {"error": f"Error en la consulta: {str(e)}"}
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        return {"error": f"Error inesperado: {str(e)}"}

# ============================================
# RUTAS DEL CHATBOT
# ============================================

@chatbot_bp.route('/')
@login_required
def chat_interface():
    """Muestra la interfaz del chat"""
    return render_template('chat.html', usuario=current_user)

@chatbot_bp.route('/send', methods=['POST'])
@login_required
def send_message():
    """
    Endpoint para chat normal (conversación general, recomendaciones)
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400

        # Obtener cliente de Groq
        client = get_groq_client()
        
        # Llamada a Groq API
        response = client.chat.completions.create(
            model=current_app.config.get('GROQ_MODEL', 'llama3-8b-8192'),
            messages=[
                {"role": "system", "content": "Eres un asistente amable para una librería llamada 'Librería Librito'. Ayudas con recomendaciones de libros, información sobre autores y géneros literarios. Responde en español de forma cálida y profesional."},
                {"role": "user", "content": user_message}
            ],
            temperature=current_app.config.get('CHATBOT_TEMPERATURE', 0.7),
            max_tokens=current_app.config.get('CHATBOT_MAX_TOKENS', 1024)
        )
        
        bot_reply = response.choices[0].message.content
        
        return jsonify({
            'reply': bot_reply,
            'mode': 'chat',
            'model': response.model
        })
        
    except Exception as e:
        logger.error(f"Error en chat normal: {str(e)}")
        return jsonify({'error': f'Error al procesar: {str(e)}'}), 500

@chatbot_bp.route('/ask-db', methods=['POST'])
@login_required
def ask_database():
    """
    Endpoint para consultas a la base de datos usando Text-to-SQL
    Solo accesible para admin y gerente
    """
    try:
        data = request.get_json()
        user_question = data.get('question', '').strip()
        
        if not user_question:
            return jsonify({'error': 'Pregunta vacía'}), 400

        # Verificar permisos
        if current_user.rol not in ['admin', 'gerente']:
            return jsonify({'error': 'No tienes permiso para consultar la base de datos'}), 403

        # Obtener cliente de Groq
        client = get_groq_client()

        # PASO 1: Groq genera la consulta SQL
        sql_response = client.chat.completions.create(
            model=current_app.config.get('GROQ_MODEL', 'llama3-8b-8192'),
            messages=[
                {"role": "system", "content": DB_SCHEMA_CONTEXT},
                {"role": "user", "content": user_question}
            ],
            temperature=current_app.config.get('CHATBOT_SQL_TEMPERATURE', 0.1),
            max_tokens=500
        )
        
        sql_query = sql_response.choices[0].message.content
        
        # PASO 2: Ejecutar la consulta usando SQLAlchemy
        result = execute_sql_query(sql_query)
        
        if "error" in result:
            return jsonify({
                'error': result["error"],
                'sql': sql_query,
                'mode': 'db_error'
            }), 400
        
        # PASO 3: Si hay resultados, formatear respuesta para el usuario
        if result["data"]:
            # Limitar a 10 filas para el contexto
            sample_data = result["data"][:10]
            
            format_response = client.chat.completions.create(
                model=current_app.config.get('GROQ_MODEL', 'llama3-8b-8192'),
                messages=[
                    {"role": "system", "content": "Eres un asistente amable de librería. Responde al usuario basado en los datos obtenidos de la base de datos. Sé conciso y profesional."},
                    {"role": "user", "content": f"Pregunta del usuario: {user_question}\n\nDatos obtenidos: {json.dumps(sample_data, indent=2, ensure_ascii=False)}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            answer = format_response.choices[0].message.content
            
            logger.info(f"Consulta BD exitosa - Usuario {current_user.id_usuario}: {result['count']} resultados")
            
            return jsonify({
                'reply': answer,
                'sql': sql_query,
                'count': result["count"],
                'data': result["data"][:5],  # Enviar solo 5 para UI
                'mode': 'db_success'
            })
        else:
            return jsonify({
                'reply': 'No encontré información que coincida con tu búsqueda en la base de datos.',
                'sql': sql_query,
                'count': 0,
                'mode': 'db_empty'
            })
            
    except Exception as e:
        logger.error(f"Error en consulta BD: {str(e)}")
        return jsonify({'error': str(e)}), 500

@chatbot_bp.route('/status', methods=['GET'])
@login_required
def chat_status():
    """Endpoint para verificar el estado del chatbot"""
    try:
        client = get_groq_client()
        return jsonify({
            'status': 'online',
            'user': current_user.usuario,
            'role': current_user.rol,
            'can_query_db': current_user.rol in ['admin', 'gerente'],
            'model': current_app.config.get('GROQ_MODEL'),
            'groq_configured': True
        })
    except Exception as e:
        return jsonify({
            'status': 'degraded',
            'groq_configured': False,
            'error': str(e)
        })