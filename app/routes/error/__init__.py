

from flask import Blueprint

error = Blueprint('error', __name__, url_prefix='error')


def load_routes():
    from app.routes.error import routes


load_routes()
