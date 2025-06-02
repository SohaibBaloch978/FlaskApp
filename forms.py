from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError, Regexp

import re

def alpha_only(form, field):
    if not re.match(r'^[A-Za-z ]+$', field.data):
        raise ValidationError('Name must contain only alphabets and spaces.')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=150), alpha_only])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=20), Regexp(r'^\d+$', message='Numbers only')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), alpha_only])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(r'^\d+$', message='Numbers only')])
    address = StringField('Address', validators=[DataRequired()])
    website = StringField('Website', validators=[Optional()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), alpha_only])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = StringField('Age', validators=[DataRequired(), Regexp(r'^\d+$', message='Only numbers allowed')])
    submit = SubmitField('Submit')