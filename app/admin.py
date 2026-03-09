from flask_login import current_user
from flask import redirect, url_for 
from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
from wtforms.validators import DataRequired, Length
from flask_admin.base import MenuLink  # <-- CORRECTO
from .extensions import admin, db
from .models import Usuario, Producto, Libro
class SecurityModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))

class UsuarioModelView(ModelView):
    column_exclude_list = ["password"]
    column_searchable_list = ['usuario', 'email']

    form_extra_fields = {
        'password': PasswordField('Contraseña', validators=[
            DataRequired(),
            Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
        ])
    }
    form_excluded_columns = ['password']

    def can_create(self):
        return current_user.rol in ['admin', 'gerente']
    
    def can_edit(self):
        return current_user.rol in ['admin', 'gerente']
    
    def can_delete(self):
        return current_user.rol == 'admin'
    
    def can_view_details(self):
        return True

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.set_password(form.password.data)
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.rol in ['admin', 'gerente']

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))

def configuracion_admin():
    admin.add_view(UsuarioModelView(Usuario, db.session))
    admin.add_view(SecurityModelView(Producto, db.session))
    admin.add_view(SecurityModelView(Libro, db.session))


    # Agrega botón en el menú lateral que apunta a tu módulo de libros
    admin.add_link(MenuLink(name="📚 Libros", url="/libros"))