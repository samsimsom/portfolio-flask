

from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/contact')

from app.routes.contact import routes
