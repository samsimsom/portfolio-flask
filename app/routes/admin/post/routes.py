

from flask import (render_template, redirect, url_for, flash,
                   request, session, g)

from app.routes.admin.post import post    # Blueprint
from app.utils.decorators import admin_required

from app.forms.form import PostForm
from app.models.post import Category
from app.models.post import Post


@post.route('/')
@admin_required
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
