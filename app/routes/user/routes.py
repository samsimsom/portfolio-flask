

from flask import render_template, session
from app.routes.user import user    # Blueprint
from app.models.user import User
from app.utils.decorators import login_required


@user.route('/<slug>')
@login_required
def profile(slug):

    email = session['user']['email']
    user = User.objects.get_or_404(email=email)

    return render_template('user/profile.html', user=user)
