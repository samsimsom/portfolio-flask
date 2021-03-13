

from flask import Blueprint

user = Blueprint('user', __name__,
                 template_folder='templates',
                 url_prefix='/user')

from app.routes.user import routes
