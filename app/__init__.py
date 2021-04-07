
from os import environ
from flask import Flask

from app.exts.database import db, session_interface


def create_app():

    app = Flask(__name__)
    app.config.from_object(environ.get('APP_CONFIG'))
    app.session_interface = session_interface(db)

    db.init_app(app)

    # Blueprint Registration
    from app.routes import (main, auth, admin, user,
                            about, contact, error, post, category)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(about)
    app.register_blueprint(contact)
    app.register_blueprint(error)
    app.register_blueprint(post)
    app.register_blueprint(category)

    return app


if __name__ == '__main__':
    create_app().run()
