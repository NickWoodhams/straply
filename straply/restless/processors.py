# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~
    restless.processors
"""

import datetime
import cPickle as pickle

from pprint import pprint
from slugify import slugify

from flask import request, render_template_string
from flask_security import login_required, current_user, login_user, \
    logout_user
from flask_restless import ProcessingException

from ..core import db
from ..frontend import create_app


def not_authorized():
    raise ProcessingException(message='Not Authorized',
                              status_code=401)


def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Methods'] = \
        'HEAD, GET, POST, PATCH, PUT, OPTIONS, DELETE'
    response.headers[
        'Access-Control-Allow-Headers'] = \
        'Origin, X-Requested-With, Content-Type, Accept'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
