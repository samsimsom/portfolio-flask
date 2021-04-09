

from flask import render_template

from app.routes.admin.user import admin_user
from app.utils.decorators import admin_required


@admin_user.route('/')
@admin_required
def index():

    return render_template('admin/user/index.html')
