

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
                                      get_current_user_username,
                                      get_current_formated_date)

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
# @admin_post.after_request
# def create_post(response):
#     if response.status_code == 200 and request.path == '/admin/post/new_post':
#         image = Image()
#         image.name = 'empty image'
#         image.path = '/empty/path'

#         post = Post()
#         post.set_author(get_current_user_id())
#         post.title = 'empty'
#         post.description = 'empty'
#         post.set_slug('empty')
#         post.set_category(id='607aea077c1a822a84ada8db')

#         post.featured_image = image
#         post.detail_images = [image]

#         post.save()
#     return response

# @admin_post.route('/')
# def index():
#     return render_template('admin/post/index.html')


@admin_post.route('/new_post', methods=['GET', 'POST'])
@admin_required
def new_post():
    form = PostForm()

    # Generate Selectionbox with current Categories
    if request.method == 'GET':
        categories = Category.objects.all()
        form.category.choices = [(category.id, category.name)
                                 for category in categories]

    if request.method == 'POST':
        # print(request.get_json())
        data = request.get_json()
        return make_response(jsonify(data))

    return render_template('admin/post/new_post.html',
                           form=form)


@admin_post.route('/upload', methods=['POST'])
@admin_required
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)

    # Create username based upload folder
    base_upload_foder_path = f'{Config.UPLOAD_PATH}'
    current_user_name = get_current_user_username()
    current_date = get_current_formated_date()
    file_path = f'{base_upload_foder_path}/{current_user_name}-{current_date}'

    if not os.path.exists(file_path):
        mode = 0o770
        parent_dir = Config.UPLOAD_PATH
        directory = f'{get_current_user_username()}-{get_current_formated_date()}'
        path = os.path.join(parent_dir, directory)
        os.makedirs(path, mode)

    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in Config.UPLOAD_EXTENSIONS or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(file_path, filename))

    return make_response(jsonify({'File Name': file_path})), 200


@admin_post.route('/upload/get_files', methods=['GET'])
@admin_required
def get_files():
    file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'\
                f'-{get_current_formated_date()}'
    files = os.listdir(file_path)
    return make_response(jsonify({'file_names': files}))


@admin_post.route('/upload/get_file/<filename>', methods=['GET'])
@admin_required
def get_file(filename):
    file_path = f'{Config.UPLOAD_PATH}/{get_current_user_username()}'\
                f'-{get_current_formated_date()}'
    files = os.listdir(file_path)

    for file in files:
        if file == filename:
            return make_response(jsonify({'fileName': file}))

    return make_response(jsonify({'file_names': files}))
