

from flask import Blueprint

post = Blueprint('post', __name__, url_prefix='/post')

from app.routes.admin.post import routes
