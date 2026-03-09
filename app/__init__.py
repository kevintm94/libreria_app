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
    from .models import Usuario
    from .admin import configuracion_admin
    from .auth import auth_bp
    from .libros import libros_bp
    configuracion_admin()
    app.register_blueprint(auth_bp)
    app.register_blueprint(libros_bp)
    return app
