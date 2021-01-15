
from flask import Flask

from .database.db import db
from .exts.ma import ma
from .routes.api.v1 import blueprint as api_v1

DATABASE = "../tmp/data.db"


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE

    app.register_blueprint(api_v1)

    ma.init_app(app)
    db.init_app(app)

    with app.app_context():
        from . import routes
        return app
