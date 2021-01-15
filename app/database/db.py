from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if __name__ == "__main__":
    from .models import *

    from app import create_app
    app = create_app()

    with app.app_context():
        db.create_all()
