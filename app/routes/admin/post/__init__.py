from flask import Blueprint

admin_post = Blueprint('admin_post', __name__, url_prefix='/admin/post')


def import_routes():
    from app.routes.admin.post import routes


import_routes()
