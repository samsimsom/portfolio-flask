

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')


def load_routes():
    from app.routes.user import routes


load_routes()
