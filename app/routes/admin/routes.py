

from flask import render_template

from app.routes.admin import admin    # Blueprint


@admin.route('/')
def index():
    return render_template('admin/index.html')
