
from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_app(application):
    db.init_app(app=application)
