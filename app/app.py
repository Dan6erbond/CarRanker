
import flask

from .database.db import db
from .exts.ma import ma

DATABASE = "../tmp/data.db"


def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE

    ma.init_app(app)
    db.init_app(app)

    with app.app_context():
        from . import routes
        return app
