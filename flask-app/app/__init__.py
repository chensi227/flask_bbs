from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
db = SQLAlchemy()


def register_blueprints(app):
    # Prevents circular imports
    from auth import mod as auth
    from main import mod as main
    from api import mod as api
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    register_blueprints(app)
    db.init_app(app)
    lm.init_app(app)
    return app