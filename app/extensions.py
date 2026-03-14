from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from groq import Groq
from flask import current_app
import logging

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="Panel Administrador")
login_manager.login_view = "login"

# Cliente de Groq (inicialización diferida)
_groq_client = None

def get_groq_client():
    """Obtiene el cliente de Groq, lo inicializa si es necesario"""
    global _groq_client
    if _groq_client is None:
        api_key = current_app.config.get('GROQ_API_KEY')
        if not api_key:
            raise RuntimeError("GROQ_API_KEY no está configurada en config.py")
        
        _groq_client = Groq(api_key=api_key)
        current_app.logger.info("✅ Cliente de Groq inicializado correctamente")
    
    return _groq_client

def init_groq_client(app):
    """Inicializa el cliente de Groq (llamado desde create_app)"""
    global _groq_client
    with app.app_context():
        try:
            api_key = app.config.get('GROQ_API_KEY')
            if api_key:
                _groq_client = Groq(api_key=api_key)
                app.logger.info("✅ Cliente Groq inicializado")
            else:
                app.logger.warning("⚠️ GROQ_API_KEY no encontrada en config.py")
        except Exception as e:
            app.logger.error(f"❌ Error inicializando Groq: {e}")