

import os
import imghdr
from slugify import slugify
from flask import (render_template,
                   redirect,
                   url_for,
                   abort,
                   send_from_directory,
                   flash,
                   make_response,
                   jsonify,
                   request)
from werkzeug.utils import secure_filename

from app.routes.admin.post import admin_post

from config import Config
from app.utils.decorators import admin_required
from app.utils.authentication import (get_current_user_id,
                                      get_current_user_username)

from app.forms.form import PostForm

from app.models.user import User
from app.models.post import Category, Post, Image


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@admin_post.errorhandler(413)
def too_large(e):
    return "File is too large", 413


# Bu blueprinte yapilan her requestden sonra,
# new_post sayfasinda ve response kodu ok ise
# Database e bos bir dokuman olusturmasini istiyorum
@admin_post.after_request
def create_post(response):
    if response.status_code == 200 and request.path == '/admin/post/new_post':
        # print('New Post Created!')
        pass
    # print(response)
    return response

# @admin_post.route('/')
# def index():
#     return render_template('admin/post/index.html')


@admin_post.route('/new_post', methods=['GET', 'POST'])
@admin_required
def new_post():
    form = PostForm()

    # Generate Selectionbox with current Categories
    categories = Category.objects.all()
    form.category.choices = [(category.id, category.name)
                             for category in categories]

    if request.method == 'POST':
        print(request.get_json())

        return make_response(jsonify('return'))

    # if form.validate_on_submit():
    #     image = Image()
    #     post = Post()
    #     post.page_id = 'test'
    #     post.set_author(get_current_user_id())
    #     post.title = form.title.data
    #     post.description = form.description.data
    #     post.set_slug(form.title.data)
    #     post.set_category(form.category.data)

    #     post.save()

    #     return redirect(url_for('admin_post.new_post'))

    return render_template('admin/post/new_post.html',
                           form=form)


@admin_post.route('/upload', methods=['POST'])
@admin_required
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    # filename = uploaded_file.filename

    # Create username based upload folder
    file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'
    if not os.path.exists(file_path):
        mode = 0o770
        parent_dir = Config.UPLOAD_PATH
        directory = get_current_user_username()
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, mode)

    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in Config.UPLOAD_EXTENSIONS or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(file_path, filename))
    return '', 204


@admin_post.route('/upload/get_files', methods=['GET'])
@admin_required
def get_files():
    file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'
    files = os.listdir(file_path)
    return make_response(jsonify({'file_names': files}))


@admin_post.route('/upload/get_file/<filename>', methods=['GET'])
@admin_required
def get_file(filename):
    file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'
    files = os.listdir(file_path)

    for file in files:
        if file == filename:
            return make_response(jsonify({'fileName': file}))

    return make_response(jsonify({'file_names': files}))


# @admin_post.route('/upload/<filename>')
# @admin_required
# def get_file(filename):
#     file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'
#     file = send_from_directory(file_path, filename)

#     return make_response(file)
