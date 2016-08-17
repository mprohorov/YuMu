import runserver
from flask_login import LoginManager


lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'signin'

def create_app(config_name):
    from .auth import auth as auth_blueprint
    runserver.app.register_blueprint(auth_blueprint)
    lm.init_app(runserver.app)

