

from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')

from app.routes.main import routes
