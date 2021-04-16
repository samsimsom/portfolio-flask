

import os
import click

from app.cli import post_cli

from app.exts.database import db
from app.models.user import User, Role
from app.models.post import Post, Category, Image


@post_cli.cli.command('drop-all')
def drop_all_colection():
    """ Drop All Collection """
    collections = db.get_db().list_collection_names()
    for collection in collections:
        db.get_db().drop_collection(collection)
    print('All Collections Record DELETED.')


@post_cli.cli.command('drop-posts')
def drop_colection():
    """ Drop Post Collection """
    Post.drop_collection()
    print('All Posts DELETED.')


@post_cli.cli.command('add-category')
@click.argument('name')
def add_role(name):
    """ Add New Post Category """
    try:
        c = Category()
        c.name = name
        c.set_slug(name)
        c.description = 'Default Description'
        c.save()
    except Exception as exp:
        print(exp)
    else:
        print(c.__repr__())
        del c


@post_cli.cli.command('list-categories')
def list_roles():
    """ List Categories """
    categories = Category.objects.all()
    print([category.name for category in categories])


@post_cli.cli.command('add-post')
@click.argument('title')
def add_post(title):
    p = Post()
    p.set_author(id='606dd753962d3cbacd9bc81a')
    p.weight = 1
    p.set_slug(title)
    p.set_category(id='607925c80b4f6a5286e8b8ed')
    p.set_title(title)

    # Featured Image
    fi = Image()
    fi.name = 'Feature Image Name'
    fi.path = '/upload/author-username/post-id/date/file-name.jpg'
    p.featured_image = fi

    # Detail Imgages
    for i in range(5):
        di = Image()
        di.name = f'Detail Image 0{i}'
        di.path = f'/upload/author-username/post-id/date/file0{i}.jpg'
        p.detail_images.append(di)

    p.save()

    print(p.__repr__())


'''
@post_cli.cli.command('list-users')
def list_users():
    """ List All Users """
    users = User.objects.all()
    print([user.username for user in users])


@post_cli.cli.command('register-user')
@click.argument('username')
@click.argument('email')
@click.argument('password')
@click.argument('role')
def register_user(username, email, password, role):
    """ Register New User """
    try:
        u = User()
        u.username = username
        u.email = email
        u.set_password(password)
        u.role = Role.objects.get(name=role.upper())
        u.save()

    except Exception as exp:
        print(exp)
    else:
        print(u.__repr__())
        del u


@post_cli.cli.command('login-user')
@click.argument('email')
@click.argument('password')
def login_user(email, password):
    """ Login User """
    try:
        u = User.objects.get(email=email)
    except User.DoesNotExist:
        u = None

    if (u is None) or not (u.check_password(password)):
        print('Invalid credentials.')
        return

    print(f'{u.__repr__()} Logged In.')
'''
