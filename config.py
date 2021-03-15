

from os import environ
from datetime import timedelta
from os.path import abspath, join, dirname
from dotenv import load_dotenv

app_base_dir = abspath(dirname(__file__))
load_dotenv(join(app_base_dir, '.env'))


class Config(object):
    # Flask
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # Mongoengine
    MONGODB_DB = environ.get('MONGODB_DB')
    MONGODB_HOST = environ.get('MONGODB_HOST')
    MONGODB_PORT = int(environ.get('MONGODB_PORT'))
    MONGODB_USERNAME = environ.get('MONGODB_USERNAME')
    MONGODB_PASSWORD = environ.get('MONGODB_PASSWORD')

    # Upload
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    UPLOAD_PATH = join(app_base_dir, 'app/static/upload')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
