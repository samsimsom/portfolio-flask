

from flask import Blueprint

app_cli = Blueprint('app-cli', __name__, cli_group='app-cli')
user_cli = Blueprint('user-cli', __name__, cli_group='user-cli')
post_cli = Blueprint('user-cli', __name__, cli_group='post-cli')


def load_cmds():
    from app.cli import app_cmds
    from app.cli import user_cmds
    from app.cli import post_cmds


load_cmds()
