# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~

    user endpoints
"""

from flask import Blueprint
from flask_login import current_user

from ..forms import userForm
from ..services import _User
from . import route


bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""
    return current_user._get_current_object()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return _User.get_or_404(user_id)


@route(bp, '/toggle-active/<user_id>')
def activate(user_id):
    """Activate a user."""
    user = _User.get_or_404(user_id)
    user.active = not user.active
    _User.save(user)
    return user
