

from flask import render_template
from app.routes.error import error


@error.app_errorhandler(404)
def not_found_error(err):
    return render_template('error/404.html'), 404


@error.app_errorhandler(500)
def internal_error(err):
    return render_template('error/500.html'), 500
