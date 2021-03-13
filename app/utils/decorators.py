

from functools import wraps
from flask import g, request, redirect, url_for, session, abort

from app.models.user import Role


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user['role']['name'] is 'ANONYMOUS':
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if g.user['role']['name'] is 'ANONYMOUS':
            return redirect(url_for('main.index'))

        if 'user' in session:
            role = Role.objects.filter(name='ADMIN').first()
            if not (session['user']['role'].name == role.name):
                return redirect(url_for('main.index'))

        return f(*args, **kwargs)
    return decorated_function
