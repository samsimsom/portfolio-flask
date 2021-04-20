from flask import Blueprint

admin_post = Blueprint('admin_post', __name__, url_prefix='/admin/post')


def load_routes():
    from app.routes.admin.post import routes


load_routes()
