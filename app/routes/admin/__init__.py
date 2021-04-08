
from flask import Blueprint

admin_post = Blueprint('admin_post', __name__, template_folder='templates',
                       url_prefix='/admin/post')

admin_main = Blueprint('admin_main', __name__, template_folder='templates',
                       url_prefix='/admin')

from app.routes.admin.main import routes
from app.routes.admin.post import routes
