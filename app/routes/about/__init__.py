

from flask import Blueprint

about = Blueprint('about', __name__, template_folder='templates',
                  url_prefix='/about')

from app.routes.about import routes
