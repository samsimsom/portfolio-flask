

from flask import render_template, redirect, url_for, abort, session, g
from app.routes.user import user    # Blueprint
from app.models.user import User
from app.utils.decorators import login_required


@user.route('/<slug>')
@login_required
def profile(slug):

    user = User.objects.get_or_404(email=g.user['email'])

    if user.slug == g.user['slug']:
        return abort(404)

    return render_template('user/profile.html', user=user)
