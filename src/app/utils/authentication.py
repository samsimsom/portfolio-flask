

from datetime import datetime
from flask import session


def add_user_in_session(id, username, email, slug, role):
    session['user'] = {'id': str(id),
                       'username': username,
                       'email': email,
                       'slug': slug,
                       'role': role}


def get_current_user():
    return session['user']


def get_current_user_id():
    return session['user']['id']


def get_current_user_username():
    return session['user']['username']


def get_current_user_email():
    return session['user']['email']


def get_current_user_slug():
    return session['user']['slug']


def get_current_user_role():
    return session['user']['role']


def get_current_formated_date() -> str:
    """
        Current formated date: 31-12-2021
    """
    return str(datetime.today().strftime('%d-%m-%Y'))


def is_in_session() -> bool:
    return session.get('user')


def is_anonymous() -> bool:
    return get_current_user_role() == 'ANONYMOUS'


def is_user() -> bool:
    return get_current_user_role() == 'USER'


def is_admin() -> bool:
    return get_current_user_role() == 'ADMIN'
