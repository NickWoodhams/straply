# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~

    users.forms
"""

from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms import TextField, PasswordField, validators, TextAreaField, SelectField, SelectMultipleField, HiddenField, RadioField, BooleanField, FileField
from wtforms.validators import DataRequired, ValidationError, Required, Optional, Length, URL, Email

from .models import User
from ..core import db


class userSettingsForm(Form):
    name = TextField('Full Name', validators=[Required()])
    email = TextField('Email', validators=[Email(), Required()])
    location = TextField('Where are you located?', validators=[Required(), Length(min=-1, max=255)], description='Ex. San Francisco, California')


userForm = model_form(User, db.session)
