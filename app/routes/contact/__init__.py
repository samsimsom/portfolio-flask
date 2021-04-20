

from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/contact')


def load_routes():
    from app.routes.contact import routes


load_routes()
