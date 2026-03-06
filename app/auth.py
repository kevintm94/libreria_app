from  flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, login_user, logout_user
from .models import User
from  .extensions import login_manager
auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@auth_bp.route('/')
def inicio():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == "POST":
        usuario = User.query.filter_by(
            username = request.form.get("nombreusuario")
        ).first()
        
        if usuario and usuario.check_password(request.form.get("contrasenia")):
            login_user(usuario)
            return redirect("/admin")
    
    return render_template("login.html")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

