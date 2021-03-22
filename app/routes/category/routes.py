

from flask import (render_template,
                   redirect,
                   url_for,
                   flash,
                   request,
                   session,
                   g)

from app.routes.category import category    # Blueprint
from app.utils.decorators import admin_required

from app.forms.form import CategoryForm
from app.models.post import Category


@category.route('/')
def index():
    return render_template('category/index.html')


@category.route('/new_category', methods=['GET', 'POST'])
@admin_required
def new_category():

    form = CategoryForm()
    if form.validate_on_submit() and request.method == 'POST':

        category = Category()
        category.name = form.name.data
        category.description = form.description.data
        category.set_slug(form.name.data)
        category.save()

        flash('Category Form Works well!')
        return redirect(url_for('category.new_category'))

    categories = Category.objects.all()

    return render_template('category/new_category.html',
                           form=form,
                           categories=categories)
