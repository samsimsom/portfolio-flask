
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def init_app(application):
    csrf.init_app(app=application)
