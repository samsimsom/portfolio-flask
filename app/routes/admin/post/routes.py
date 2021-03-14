

from flask import render_template

from app.routes.admin.post import post    # Blueprint
from app.utils.decorators import admin_required

from app.forms.form import PostForm


@post.route('/')
@admin_required
def index():
    return render_template('post/index.html')


@post.route('/new_post')
@admin_required
def new_post():

    form = PostForm()

    return render_template('post/new_post.html', form=form)
