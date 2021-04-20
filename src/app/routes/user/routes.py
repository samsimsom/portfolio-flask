

from flask import render_template
from app.routes.user import user
from app.models.user import User

from app.utils.authentication import get_current_user_username
from app.utils.decorators import login_required


@user.route('/<slug>')
@login_required
def profile(slug):

    user = User.objects.get_or_404(slug=slug)

    return render_template('user/profile.html', user=user)
