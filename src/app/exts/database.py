
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

db = MongoEngine()


def init_app(application):
    db.init_app(app=application)


def session_interface(database):
    return MongoEngineSessionInterface(database)
