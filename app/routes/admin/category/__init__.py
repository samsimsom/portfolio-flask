

from flask import Blueprint

admin_category = Blueprint('admin_category', __name__, url_prefix='/admin/category')

from app.routes.admin.category import routes
