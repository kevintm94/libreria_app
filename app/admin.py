from flask_login import current_user
from flask import redirect, url_for 
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import MenuLink  # <-- CORRECTO
from .extensions import admin, db
from .models import User, Producto, Libro
class SecurityModelView(ModelView):
    column_exclude_list = ["password"]
    
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))

def configuracion_admin():
    admin.add_view(SecurityModelView(User, db.session))
    admin.add_view(SecurityModelView(Producto, db.session))
    admin.add_view(SecurityModelView(Libro, db.session))


    # Agrega botón en el menú lateral que apunta a tu módulo de libros
    admin.add_link(MenuLink(name="📚 Libros", url="/libros"))