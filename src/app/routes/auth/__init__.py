

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')


def load_routes():
    from app.routes.auth import routes


load_routes()
