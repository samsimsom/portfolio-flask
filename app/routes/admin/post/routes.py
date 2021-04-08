
import imghdr
import os
from flask import (render_template,
                   redirect,
                   url_for,
                   abort,
                   send_from_directory,
                   flash,
                   request,
                   session,
                   g)
from werkzeug.utils import secure_filename

from app.routes.admin import admin_post
from app.utils.decorators import admin_required


@admin_post.route('/')
@admin_required
def index():
    return render_template('post/index.html')
