
from flask import Blueprint

admin_user = Blueprint('admin_user', __name__, url_prefix='/admin/user')

from app.routes.admin.user import routes
