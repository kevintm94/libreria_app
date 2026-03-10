from flask_login import UserMixin
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    id_usuario = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(50), unique=True, nullable = False)
    password = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    nombre_completo = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), default = 'vendedor')


    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return self.id_usuario
    
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(150), nullable = False)
    descripcion = db.Column(db.Text, nullable = False)
    precio = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return self.nombre

class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(20), unique=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(100))
    anio_publicacion = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    descripcion = db.Column(db.Text)
    paginas = db.Column(db.Integer)
    idioma = db.Column(db.String(30), default="Español")

    def __repr__(self):
        return f"<Libro {self.titulo}>"

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.Text)

    def __repr__(self):
        return f"<Cliente {self.nombre} {self.apellido}>"


# --- Nuevos modelos para ventas ---
class Venta(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_venta = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    total = db.Column(db.Numeric(10, 2), nullable=False)
    metodo_pago = db.Column(db.Enum('efectivo', 'tarjeta', 'transferencia', 'otros', name='metodo_pago_enum'), default='efectivo')

    cliente = db.relationship('Cliente', backref=db.backref('ventas', lazy=True))
    usuario = db.relationship('Usuario', backref=db.backref('ventas', lazy=True))
    detalles = db.relationship('DetalleVenta', backref='venta', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Venta {self.id_venta} - Cliente {self.id_cliente}>"

class DetalleVenta(db.Model):
    id_detalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('venta.id_venta'), nullable=False)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id_libro'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)

    libro = db.relationship('Libro', backref=db.backref('detalles_venta', lazy=True))

    def __repr__(self):
        return f"<DetalleVenta {self.id_detalle} - Venta {self.id_venta}>"