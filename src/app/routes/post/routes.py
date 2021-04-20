

from flask import render_template

from app.routes.post import post

from app.forms.form import PostForm

from app.models.post import Category
from app.models.post import Post


@post.route('/')
def index():
    return render_template('post/index.html')
