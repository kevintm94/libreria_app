from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            usuario = User(username="admin", role="admin")
            usuario.set_password('1234')
            db.session.add(usuario)
            db.session.commit()
    app.run(debug=True)