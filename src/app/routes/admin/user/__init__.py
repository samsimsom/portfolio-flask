
from flask import Blueprint

admin_user = Blueprint('admin_user', __name__, url_prefix='/admin/user')


def load_routes():
    from app.routes.admin.user import routes


load_routes()
