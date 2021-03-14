

import re
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     BooleanField,
                     SubmitField,
                     TextAreaField,
                     MultipleFileField,
                     SelectField)
from wtforms.validators import (ValidationError,
                                DataRequired,
                                Email,
                                EqualTo,
                                Optional,
                                Length)
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.models.user import User


# ------------------------------------------------------------------------------
# AUTH FROMS
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if not re.match("^[a-zA-Z]*$", username.data):
            raise ValidationError('[a-z A-Z]')

        try:
            user = User.objects.get(username=username.data)
        except User.DoesNotExist:
            user = None

        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        try:
            user = user = User.objects.get(email=email.data)
        except User.DoesNotExist:
            user = None

        if user is not None:
            raise ValidationError('Please use a different email address.')


# ------------------------------------------------------------------------------
# POST FROMS
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    description = TextAreaField(
        'Description',
        validators=[Optional(), Length(max=1024)])

    category = SelectField('Category',
                           choices=[(1, "Group1"), (2, "Group2")],
                           validators=[DataRequired()])

    featured_image = FileField(
        'Featureed Image',
        validators=[FileRequired(),
                    FileAllowed(['jpg', 'png'], 'Images only!')])

    detail_images = MultipleFileField(
        'Detail Images',
        validators=[FileRequired(),
                    FileAllowed(['jpg', 'png'], 'Images only!')])

    submit = SubmitField('New Post')
