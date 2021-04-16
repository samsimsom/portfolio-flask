

from uuid import uuid4

from flask import session

from app import create_app

from app.utils.authentication import (get_current_user,
                                      get_current_user_role,
                                      is_anonymous,
                                      is_user,
                                      is_admin,
                                      add_user_in_session)


app = create_app()


# ------------------------------------------------------------------------------
# APP REQUESTS
@app.before_request
def before_app_request():
    if not session.get('user'):
        add_user_in_session(uuid4(), 'anonymous',
                            'anonymous@mail.com', 'anonymous',
                            'ANONYMOUS')


# ------------------------------------------------------------------------------
# CONTEXT PROCESSORS
@app.context_processor
def ctp_current_user():
    return dict(current_user=get_current_user())


@app.context_processor
def ctp_current_user_role():
    return dict(current_user_role=get_current_user_role())


@app.context_processor
def ctp_is_anonymous():
    return dict(is_anonymous=is_anonymous())


@app.context_processor
def ctp_is_user():
    return dict(is_user=is_user())


@app.context_processor
def ctp_is_admin():
    return dict(is_admin=is_admin())
