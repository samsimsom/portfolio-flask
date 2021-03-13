

from flask import render_template

from app.routes.admin import admin    # Blueprint
from app.utils.decorators import admin_required


@admin.route('/')
@admin_required
def index():

    return render_template('admin/index.html')
