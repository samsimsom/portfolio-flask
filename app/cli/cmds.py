

import os
import click
from app.exts.database import db
from app.models.user import User, Role
from app.models.post import Category, Comment, Post


def register(app):
    @app.cli.group()
    def database():
        """Database commands."""
        pass

    @database.command('drop-user')
    def drop_colection():
        """Drop User Collection"""
        User.drop_collection()
        print('All Users Record DELETED.')

    @database.command('add-role')
    @click.argument('name')
    def add_role(name):
        """Add New Role"""
        r = Role()
        r.name = name
        r.save()

        print(f'{r.name} | added.')

    @database.command('list-role')
    def list_role():
        """List All Role"""
        r = Role.objects.all()
        print([role.name for role in r])

    @database.command('register-user')
    @click.argument('username')
    @click.argument('email')
    @click.argument('password')
    @click.argument('role')
    def register_user(username, email, password, role):
        """Register New User"""
        u = User()
        u.username = username
        u.email = email
        u.set_password(password)
        u.role = Role.objects.get(name=role)
        u.save()

        print(f'User | {u.username} > document created.')

    @database.command('login-user')
    @click.argument('email')
    @click.argument('password')
    def login_user(email, password):
        """Login User"""
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            u = None

        if (u is None) or not (u.check_password(password)):
            print('Invalid credentials.')
            return

        print('Login.')

# ------------------------------------------------------------------------------

    @database.command('add-category')
    @click.argument('name')
    def add_category(name):
        """Add New Category"""
        c = Category()
        c.name = name
        c.slug = c.set_slug(name)
        c.save()

        print('New category added.')

    @database.command('add-post')
    @click.argument('author')
    @click.argument('title')
    @click.argument('description')
    @click.argument('slug')
    def add_post(author, title, description, slug):
        """Add New Post"""
        p = Post()
        p.author = User.objects.get(username=author)
        p.title = title
        p.slug = p.set_slug(title)
        p.description = description
        p.category = [Category.objects.get(slug=slug)]
        p.save()

        print('New Post added.')
