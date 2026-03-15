from  flask import Blueprint, redirect, url_for, render_template, request, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from .models import Usuario
from  .extensions import login_manager
auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    # Si la petición es AJAX/JSON, devuelve un error 401 en JSON en lugar de redirigir.
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
        return jsonify(error='Se requiere autenticación para esta acción.'), 401
    # De lo contrario, para peticiones normales, redirige a la página de login.
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
def inicio():
    return redirect(url_for('ventas.dashboard') if current_user.is_authenticated else url_for('auth.login'))

@auth_bp.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(
            usuario = request.form.get("nombreusuario")
        ).first()
        
        if usuario and usuario.check_password(request.form.get("contrasenia")):
            login_user(usuario)
            return redirect(url_for("ventas.dashboard"))
    
    return render_template("login.html")
@login_required
@auth_bp.route('/logout') 
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

#@auth_bp.route("/productos")
#def productos():
#    lista_productos = Producto.query.all()
#    return render_template("productos.html", productos = lista_productos)
