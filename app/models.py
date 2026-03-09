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