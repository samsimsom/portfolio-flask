

from functools import wraps
from flask import redirect, url_for, request

from app.models.user import User, Role

from app.utils.authentication import (is_anonymous,
                                      is_admin,
                                      get_current_user_id)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            user = User.objects.filter(id=get_current_user_id()).first()
        except:
            user = None

        if is_anonymous() or user is None:
            return redirect(url_for('auth.login', next=request.url))

        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            user = User.objects.filter(id=get_current_user_id()).first()
        except:
            user = None

        if user is None or not is_admin() or not user.role.name == 'ADMIN':
            return redirect(url_for('main.index'))

        return f(*args, **kwargs)
    return decorated_function
