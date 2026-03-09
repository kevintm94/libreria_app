from app import create_app
from app.extensions import db
from app.models import Usuario

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Usuario.query.filter_by(usuario="admin").first():
            usuario = Usuario(usuario="admin", rol="admin", email = "admi@gmail.com", nombre_completo = "Administrador")
            usuario.set_password('1234')
            db.session.add(usuario)
            db.session.commit()
    app.run(debug=True)