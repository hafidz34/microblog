from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login"  # redirect ke /login bila belum login

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)

    # import models & routes SETELAH init extensions,
    # dan lakukan dalam app_context untuk menghindari circular import
    with app.app_context():
        from . import models, routes  # noqa: F401
        db.create_all()

    return app
