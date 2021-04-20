
from flask import Blueprint

admin_main = Blueprint('admin_main', __name__, url_prefix='/admin')


def load_routes():
    from app.routes.admin.main import routes


load_routes()
