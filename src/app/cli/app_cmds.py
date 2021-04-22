

import os
import click

from flask import current_app, g
from flask.cli import with_appcontext

from app.cli import app_cli

from app.exts.database import db


@app_cli.cli.command('app-context')
@with_appcontext
def app_context():
    """ Application Context """
    template = {
        'current_app': current_app,
        'g': iter(g)
    }
    print(template)
