from  flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, login_user, logout_user
from .models import Usuario
from  .extensions import login_manager
auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@auth_bp.route('/')
def inicio():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == "POST":
        usuario = Usuario.query.filter_by(
            usuario = request.form.get("nombreusuario")
        ).first()
        
        if usuario and usuario.check_password(request.form.get("contrasenia")):
            login_user(usuario)
            return redirect("/dashboard")
    
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
