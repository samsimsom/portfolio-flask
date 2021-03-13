

import re
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     BooleanField,
                     SubmitField)
from wtforms.validators import (ValidationError,
                                DataRequired,
                                Email,
                                EqualTo)
from app.models.user import User


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
        if not re.match("^[a-zA-Z\s]*$", username.data):
            raise ValidationError('[a-z A-Z and space]')

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
