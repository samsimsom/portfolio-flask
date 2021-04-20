

from flask import render_template
from app.routes.contact import contact


@contact.route('/')
def index():
    return render_template('contact/index.html')
