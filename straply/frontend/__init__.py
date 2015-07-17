# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~

    frontend application factory
"""

from functools import wraps
from flask import render_template
from flask.ext.logging import Filter

from flask.ext.admin import Admin, BaseView, AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView
from ..admin.views import AdminModel, UserView, MyHomeView

from raven.contrib.flask import Sentry

from .. import factory
from ..core import db
from ..models import Role, User
from ..helpers import gravatar, format_currency, nl2br, firstname, pretty_date, \
    current_date

# Disable the double password confirm on the user registration form
from flask_security.forms import PasswordConfirmFormMixin
PasswordConfirmFormMixin.password_confirm = False


def create_app(settings_override=None):
    """Returns the straply dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)
    Sentry(app)
    admin = Admin(app, index_view=MyHomeView())
    admin.add_view(UserView(db.session, category="Users"))
    admin.add_view(AdminModel(Role, db.session, category="Users"))

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    # Filter out static requests
    Filter('static')

    # Register some custom app filters
    app.jinja_env.filters['gravatar'] = gravatar
    app.jinja_env.filters['format_currency'] = format_currency
    app.jinja_env.filters['nl2br'] = nl2br
    app.jinja_env.filters['firstname'] = firstname
    app.jinja_env.filters['pretty_date'] = pretty_date
    app.jinja_env.globals.update(current_date=current_date())
    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
