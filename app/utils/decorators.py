

from functools import wraps
from flask import g, request, redirect, url_for, session, abort

from app.models.user import Role


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if g.user is None:
            return redirect(url_for('main.index'))

        if 'user' in session:
            if not (g.user['role'] == Role.objects.get(
                    id='604b33ba15fc7533e3383861')):
                return abort(403)

        return f(*args, **kwargs)
    return decorated_function
