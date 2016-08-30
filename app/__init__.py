from flask import Flask

from flask_bootstrap import Bootstrap
from flask_login import LoginManager

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'signin'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.secret_key = 's3cr3t'
    lm.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from . import main as main_bp
    app.register_blueprint(main_bp)

    return app


