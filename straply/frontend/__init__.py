# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~

    frontend application factory
"""

from functools import wraps

from flask.ext.superadmin import Admin
from raven.contrib.flask import Sentry

from .. import factory
from ..core import db
from ..models import *
from ..helpers import gravatar



def create_app(settings_override=None):
    """Returns the straply dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)
    sentry = Sentry(app)
    admin = Admin(app)
    admin.register(User, session=db.session)
    admin.register(Role, session=db.session)
    #register some custom app filters
    app.jinja_env.filters['gravatar'] = gravatar
    return app


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
