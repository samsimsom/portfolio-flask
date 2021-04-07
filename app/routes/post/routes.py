

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

from app.routes.post import post
from config import Config
from app.utils.decorators import admin_required

from app.forms.form import PostForm

from app.models.post import Category
from app.models.post import Post


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@post.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@post.route('/')
def index():
    return render_template('post/index.html')


@post.route('/new_post', methods=['GET', 'POST'])
@admin_required
def new_post():
    form = PostForm()
    categories = Category.objects.all()
    form.category.choices = [(x.id, x.name) for x in categories]

    if form.validate_on_submit():
        post = Post()
        post.set_author(g.user['id'])
        post.title = form.title.data
        post.description = form.description.data
        post.set_slug(form.title.data)
        post.set_category(form.category.data)
        post.save()

        return redirect(url_for('post.new_post'))

    return render_template('post/new_post.html', form=form)


@post.route('/upload', methods=['POST'])
@admin_required
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in Config.UPLOAD_EXTENSIONS or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(Config.UPLOAD_PATH, filename))
    return '', 204


@post.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(Config.UPLOAD_PATH, filename)


@post.route('/files')
def files():
    files = os.listdir(Config.UPLOAD_PATH)
    return render_template('post/index.html', files=files)
