
import os
from dotenv import load_dotenv

from flask import Flask

from app.exts.database import db, session_interface
from app.exts.csrf import csrf

app_base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(app_base_dir, '.env'))


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_CONFIG'))
    # app.session_interface = session_interface(db)

    db.init_app(app)
    csrf.init_app(app)

    # Blueprint Registration
    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.admin.main import admin_main
    app.register_blueprint(admin_main)

    from app.routes.admin.post import admin_post
    app.register_blueprint(admin_post)

    from app.routes.admin.category import admin_category
    app.register_blueprint(admin_category)

    from app.routes.admin.user import admin_user
    app.register_blueprint(admin_user)

    from app.routes.user import user
    app.register_blueprint(user)

    from app.routes.about import about
    app.register_blueprint(about)

    from app.routes.contact import contact
    app.register_blueprint(contact)

    from app.routes.error import error
    app.register_blueprint(error)

    from app.routes.post import post
    app.register_blueprint(post)

    from app.cli import app_cli, user_cli, post_cli
    app.register_blueprint(app_cli)
    app.register_blueprint(user_cli)
    app.register_blueprint(post_cli)

    return app


if __name__ == '__main__':
    create_app().run()
