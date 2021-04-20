

from flask import render_template

from app.routes.admin.main import admin_main
from app.utils.decorators import admin_required


@admin_main.route('/')
@admin_required
def index():

    return render_template('admin/main/index.html')
