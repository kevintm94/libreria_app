from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask import current_app
from groq import Groq

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="Panel Administrador")
login_manager.login_view = "login"

def init_groq_client(app):
    """Inicializa el cliente de Groq y lo adjunta al objeto de la aplicación."""
    api_key = app.config.get('GROQ_API_KEY')
    if api_key:
        # Adjuntamos el cliente al objeto 'app' para que sea accesible globalmente
        # a través de 'current_app'.
        app.groq_client = Groq(api_key=api_key)
    else:
        app.groq_client = None
        print("ADVERTENCIA: GROQ_API_KEY no está configurada. El chatbot y análisis IA no funcionarán.")

def get_groq_client():
    """
    Función de conveniencia para obtener el cliente Groq desde el contexto actual.
    Esto unifica el acceso desde diferentes módulos.
    """
    return getattr(current_app, 'groq_client', None)