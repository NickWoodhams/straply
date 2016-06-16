# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~
    restless api
"""

import hashlib
import flask_restless

from pprint import pprint

from flask import request
from flask_restless import ProcessingException
from flask_security import login_required, current_user, login_user, \
    logout_user
from raven.contrib.flask import Sentry

from .. import factory
from ..core import db
from ..models import User
from .processors import not_authorized, add_cors_header


def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the straply API application instance"""

    app = factory.create_app(
        __name__, __path__, settings_override,
        register_security_blueprint=register_security_blueprint)

    # Start Sentry
    Sentry(app)

    manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(
        User,
        url_prefix='/api/1.0',
        methods=['GET'],
        preprocessors={
            'PUT_SINGLE': [],
            'PUT_MANY': [not_authorized]
        },
        postprocessors={
            'GET_SINGLE': [],
            'GET_MANY': [not_authorized]
        }
    )
    app.after_request(add_cors_header)
    return app
