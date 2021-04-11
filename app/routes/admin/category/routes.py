

from flask import (render_template,
                   redirect,
                   url_for,
                   flash,
                   make_response,
                   jsonify,
                   request)

from app.routes.admin.category import admin_category
from app.utils.decorators import admin_required

from app.forms.form import CategoryForm, EmptyForm
from app.models.post import Category


@admin_category.route('/')
def index():
    return render_template('admin/category/index.html')


@admin_category.route('/new_category', methods=['GET'])
@admin_required
def new_category():
    form = CategoryForm()
    empty_form = EmptyForm()
    return render_template('admin/category/new_category.html',
                           form=form,
                           empty_form=empty_form)


@admin_category.route('/get_categories', methods=['GET'])
@admin_required
def get_categories():
    categories = Category.objects.all()
    return make_response(jsonify(categories))


@admin_category.route('/get_category/<id>', methods=['GET'])
@admin_required
def get_category(id):
    category = Category.objects.get(id=id)
    return make_response(jsonify(category))


@admin_category.route('/add_category', methods=['POST'])
@admin_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        content = request.get_json()
        if content is not None:
            category = Category()
            category.name = content['name']
            category.description = content['description']
            category.set_slug(content['name'])
            category.save()
            category_id = str(category.id)
            return make_response(jsonify({'Success': category_id}))
        else:
            return make_response(jsonify({'Error': 'Request Content None'}))
    else:
        return make_response(jsonify({'Error': form.errors}))


# @admin_category.route('/edit_category/<id>', methods=['POST'])
# @admin_required
# def edit_category():
#     categories = Category.objects.all()
#     return make_response(jsonify(categories))


@admin_category.route('/delete_category/<id>', methods=['DELETE'])
@admin_required
def delete_category(id):

    category = Category.objects.get(id=id)
    category.delete()

    return make_response(jsonify({'id': id, 'delete': 'ok'}))
