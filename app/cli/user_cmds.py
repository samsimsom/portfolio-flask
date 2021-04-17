

import os
import click

from app.cli import user_cli

from app.exts.database import db
from app.models.user import User, Role


@user_cli.cli.command('drop-all')
def drop_all_colection():
    """ Drop All Collection """
    collections = db.get_db().list_collection_names()
    for collection in collections:
        db.get_db().drop_collection(collection)
    print('All Collections Record DELETED.')


@user_cli.cli.command('drop-user')
def drop_colection():
    """ Drop User Collection """
    User.drop_collection()
    print('All Users Record DELETED.')


@user_cli.cli.command('add-role')
@click.argument('name')
def add_role(name):
    """ Add New User Role """
    try:
        r = Role()
        r.set_name(name)
        r.description = 'Default Description'
        r.save()
    except Exception as exp:
        print(exp)
    else:
        print(r.__repr__())
        del r


@user_cli.cli.command('list-roles')
def list_roles():
    """ List All Role """
    roles = Role.objects.all()
    print([role.name for role in roles])


@user_cli.cli.command('list-users')
def list_users():
    """ List All Users """
    users = User.objects.all()
    print([user.username for user in users])


@user_cli.cli.command('register-user')
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
        u.set_slug(username)
        u.role = Role.objects.get(name=role.upper())
        u.save()

    except Exception as exp:
        print(exp)
    else:
        print(u.__repr__())
        del u


@user_cli.cli.command('login-user')
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
