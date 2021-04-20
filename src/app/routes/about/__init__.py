

from flask import Blueprint

about = Blueprint('about', __name__, url_prefix='/about')


def load_routes():
    from app.routes.about import routes


load_routes()
