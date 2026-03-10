import pymysql

from app.admin import configuracion_admin
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
from .extensions import db, login_manager, admin

def create_app():
    app = Flask (__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    admin.init_app(app)
    from .models import Usuario, Cliente
    from .admin import configuracion_admin
    from .auth import auth_bp
    from .libros import libros_bp
    from .clientes import clientes_bp
    from .ventas import ventas_bp
    configuracion_admin()
    app.register_blueprint(auth_bp)
    app.register_blueprint(libros_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(ventas_bp)
    return app
