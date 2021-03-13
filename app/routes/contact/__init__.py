

from flask import Blueprint

contact = Blueprint('contact', __name__, template_folder='templates',
                    url_prefix='/contact')

from app.routes.contact import routes
