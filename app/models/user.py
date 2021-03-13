

from datetime import datetime
from slugify import slugify
from hashlib import md5
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from app.exts.database import db


class Role(db.Document):
    name = db.StringField(max_length=64, required=True, unique=True)
    description = db.StringField()

    meta = {'collection': 'role'}


class User(db.Document):
    username = db.StringField(max_length=64, required=True, unique=True)
    email = db.EmailField(max_length=128, required=True, unique=True)
    password_hash = db.StringField(max_length=128, required=True)
    slug = db.StringField(max_length=128)
    role = db.ReferenceField(Role, reverse_delete_rule=db.CASCADE)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'user', 'indexes': ['username',
                                              'email',
                                              '-creation_date']}

    def __repr__(self) -> str:
        return f'<User | username: {self.username}, email: {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_slug(self, username):
        self.slug = slugify(username)

    def set_username(self, username):
        self.username = ' '.join(str(username).split()).lower()

    def set_email(self, email):
        self.email = str(email).lower()
