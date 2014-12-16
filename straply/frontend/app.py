# -*- coding: utf-8 -*-
"""
    Straply
    ~~~~~~~~

    Main views
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_security import login_required, current_user, login_user, logout_user

from . import route
from ..core import db
from ..services import _User
from ..models import User
from ..forms import userSettingsForm


bp = Blueprint('main', __name__)


@route(bp, '/')
def index():
    """Returns the index."""
    return render_template('index.html')


@route(bp, '/preferences', methods=['GET', 'POST'])
@login_required
def preferences():
    """Allows user to change account prefs"""
    form = userSettingsForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Successfully updated your profile', 'success')
    return render_template('preferences.html', form=form)
