import os

from flask import Flask

from .database.db import db
from .exts.ma import ma
from .routes.api.v1 import blueprint as api_v1

def get_database_url():
    postgres_password = os.getenv('POSTGRES_PASSWORD')

    # Use Docker secrets configuration
    if os.getenv('POSTGRES_PASSWORD_FILE'):
        f = open(os.getenv('POSTGRES_PASSWORD_FILE'))
        postgres_password = f.readline()
        f.close()

    return f"postgresql://{os.getenv('POSTGRES_USER')}:{postgres_password}@localhost:5432/os.getenv('POSTGRES_DB')"


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()

    app.register_blueprint(api_v1)

    ma.init_app(app)
    db.init_app(app)

    with app.app_context():
        from . import routes
        return app
