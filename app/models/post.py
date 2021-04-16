

from time import time
from datetime import datetime
from slugify import slugify
from app.exts.database import db
from app.models.user import User


# ------------------------------------------------------------------------------
# CATEGORY MODEL
class Category(db.Document):
    name = db.StringField(max_length=128, required=True, unique=True)
    slug = db.StringField(max_length=128)
    description = db.StringField(max_length=512)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'category', 'indexes': ['name', 'slug']}

    def __repr__(self):
        return f'<Category | Name: {self.name} Slug: {self.slug}>'

    def set_slug(self, name):
        self.slug = slugify(name)


# ------------------------------------------------------------------------------
# IMAGE MODEL
class Image(db.EmbeddedDocument):
    name = db.StringField(max_length=128, required=True)
    path = db.StringField(max_length=256, required=True)


# ------------------------------------------------------------------------------
# POST MODEL
class Post(db.Document):

    author = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)
    creation_date = db.DateTimeField(default=datetime.utcnow())
    weight = db.IntField(min_value=0, default=0)
    slug = db.StringField(max_length=128)
    category = db.ReferenceField(Category)

    title = db.StringField(max_length=128, required=True)
    description = db.StringField(max_length=1024)

    featured_image = db.ListField(db.EmbeddedDocumentField(Image))
    detail_images = db.ListField(db.EmbeddedDocumentField(Image))

    meta = {'collection': 'post', 'indexes': ['title', 'slug']}

    def __repr__(self):
        return f'<Post | Title: {self.title} Author:{self.author} \
                 Slug: {self.slug}>'

    def set_slug(self, title):
        self.slug = slugify(title)

    def set_category(self, id):
        self.category = Category.objects.filter(id=id).first()

    def set_author(self, id):
        self.author = User.objects.filter(id=id).first()
