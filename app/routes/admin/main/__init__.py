
from flask import Blueprint

admin_main = Blueprint('admin_main', __name__, url_prefix='/admin')

from app.routes.admin.main import routes
