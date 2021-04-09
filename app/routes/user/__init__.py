

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

from app.routes.user import routes
