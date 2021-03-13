

from time import time
from datetime import datetime
from slugify import slugify
from app.exts.database import db
from app.models.user import User


class Category(db.Document):
    name = db.StringField(max_length=128, required=True, unique=True)
    slug = db.StringField(max_length=128)
    description = db.StringField(max_length=512)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'category', 'indexes': ['name', 'slug']}

    def __repr__(self):
        return f'<Category | Name: {self.name} Slug: {self.slug}>'

    def set_slug(self, name):
        return slugify(name)


class Comment(db.Document):
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
    comment = db.StringField(max_length=1024)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'comment'}


class Post(db.Document):
    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
    title = db.StringField(max_length=128, required=True)
    slug = db.StringField(max_length=128)
    description = db.StringField(max_length=1024)
    creation_date = db.DateTimeField(default=datetime.utcnow())
    weight = db.IntField(min_value=0)
    category = db.ListField(db.ReferenceField(Category,
                                              reverse_delete_rule=db.CASCADE))

    meta = {'collection': 'post', 'indexes': ['title', 'slug']}

    def __repr__(self):
        return f'<Post | Title: {self.title} Author:{self.author} \
                 Slug: {self.slug}>'

    def set_slug(self, title):
        return slugify(title)
