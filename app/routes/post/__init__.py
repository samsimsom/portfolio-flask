

from flask import Blueprint

post = Blueprint('post', __name__, url_prefix='/post')


def load_routes():
    from app.routes.post import routes


load_routes()
