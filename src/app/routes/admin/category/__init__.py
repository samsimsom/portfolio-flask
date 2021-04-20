

from flask import Blueprint

admin_category = Blueprint('admin_category', __name__,
                           url_prefix='/admin/category')


def load_routes():
    from app.routes.admin.category import routes


load_routes()
