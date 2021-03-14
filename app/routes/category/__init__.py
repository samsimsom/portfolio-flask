

from flask import Blueprint

category = Blueprint('category', __name__, template_folder='templates',
                     url_prefix='/category')

from app.routes.category import routes
