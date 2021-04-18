

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
from app.models.post import Category


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
# POST FROM
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    description = TextAreaField('Description',
                                validators=[Length(max=1024)])

    category = SelectField('Category',
                           choices=[],
                           validators=[DataRequired()])

    featured_image = FileField(
        'Featured Image',
        validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    detail_images = MultipleFileField(
        'Detail Images',
        validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    save = SubmitField('Save')
    submit = SubmitField('Publish')


# ------------------------------------------------------------------------------
# CATEGORY FROM
class CategoryForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])

    description = TextAreaField('Description',
                                validators=[Length(max=1024)])

    submit = SubmitField('New Category')

    def validate_name(self, name):
        try:
            category = Category.objects.get(name=name.data)
        except Category.DoesNotExist:
            category = None

        if category is not None:
            raise ValidationError('Please use a different category name.')


# ------------------------------------------------------------------------------
# EMPTY FROM
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
