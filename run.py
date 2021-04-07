

from flask import g, session
from app import create_app, db
from app.cli import cmds
from app.models.user import User, Role
from app.models.post import Post


app = create_app()
cmds.register(app)


# ------------------------------------------------------------------------------
# APP REQUESTS
@app.before_request
def before_app_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
    else:
        g.user = {'id': 'anonymous',
                  'username': 'anonymous',
                  'slug': 'anonymous',
                  'email': 'anonymous',
                  'role': {'name': 'ANONYMOUS'}}


# ------------------------------------------------------------------------------
# CONTEXT PROCESSORS
# Jinja template icerinde kullanabilecegin current_user
# degiskenini olusturuyor.
@app.context_processor
def get_current_user():
    return dict(current_user=g.user)


# Jinja template icerinde kullanabilecegin role
# degiskenini olusturuyor.
@app.context_processor
def db_utilities():
    def get_user_role(name):
        role = Role.objects.filter(name=name).first()
        if role is None:
            role = {'name': 'USER'}
            return role
        return role.name
    return dict(role=get_user_role)


# ------------------------------------------------------------------------------
# SHELL CONTEXT PROCESSORS
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
