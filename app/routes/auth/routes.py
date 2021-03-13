

from flask import (render_template, redirect, url_for, flash,
                   request, session, g)
from werkzeug.urls import url_parse

from app.routes.auth import auth    # Blueprint
from app.forms.form import LoginForm, RegistrationForm
from app.models.user import User, Role
from app.utils.decorators import login_required


@auth.before_app_request
def before_app_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if 'user' in session:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit() and request.method == 'POST':

        user = User.objects.filter(email=form.email.data.lower()).first()

        if (user is None) or not (user.check_password(form.password.data)):
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))

        # User Login and Remeber_Me
        session['user'] = {'username': user.username,
                           'slug': user.slug,
                           'email': user.email}
        if form.remember_me.data:
            session.permanent = True
        else:
            session.permanent = False

        next_page = request.form.get('next_page')
        print(next_page)
        if (not next_page) and (url_parse(next_page).netloc != ''):
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('auth/login.html',
                           form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if 'user' in session:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit() and request.method == 'POST':
        user = User()
        user.set_username(form.username.data)
        user.set_email(form.email.data)
        user.set_password(form.password.data)
        user.set_slug(user.username)
        user.role = Role.objects.get(id='604b33c1337f0cdd73f39995')  # FIXME:
        user.save()

        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',
                           form=form)


@auth.route('/logout')
@login_required
def logout():
    if 'user' in session:
        session.pop('user', None)

    return redirect(url_for('main.index'))
