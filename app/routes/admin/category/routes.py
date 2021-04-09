

from flask import (render_template,
                   redirect,
                   url_for,
                   flash,
                   make_response,
                   jsonify,
                   request)

from app.routes.admin.category import admin_category
from app.utils.decorators import admin_required

from app.forms.form import CategoryForm
from app.models.post import Category


@admin_category.route('/')
def index():
    return render_template('admin/category/index.html')


@admin_category.route('/new_category', methods=['GET', 'POST'])
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
        return redirect(url_for('admin_category.new_category'))

    categories = Category.objects.all()

    return render_template('admin/category/new_category.html',
                           form=form,
                           categories=categories)


@admin_category.route('/get_category', methods=['GET'])
@admin_required
def get_category():
    categories = Category.objects.all()
    return make_response(jsonify(categories))


@admin_category.route('/edit_category/<id>', methods=['POST'])
@admin_required
def edit_category():
    categories = Category.objects.all()
    return make_response(jsonify(categories))


@admin_category.route('/delete_category/<id>', methods=['POST'])
@admin_required
def delete_category():
    categories = Category.objects.all()
    return make_response(jsonify(categories))
