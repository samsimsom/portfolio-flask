

from flask import render_template, redirect, url_for
from app.routes.main import main


@main.route('/')
def index():
    return redirect(url_for('post.index'))
