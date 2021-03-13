

from flask import Blueprint

error = Blueprint('error', __name__,
                  template_folder='templates',
                  url_prefix='error')

from app.routes.error import routes
