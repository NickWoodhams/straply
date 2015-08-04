# -*- coding: utf-8 -*-
"""
    wsgi
    ~~~~

    straply wsgi module
"""

# auto Alembic
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))
from subprocess import Popen, PIPE, STDOUT

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from straply import api, frontend, restless

frontend_app = frontend.create_app()
api_app = api.create_app()
restless_app = restless.create_app()


@frontend_app.before_first_request
def setup_app():
    from straply.models import User, Role
    from straply.core import db
    if not Role.query.filter_by(name="admin").count():
        role = Role(name="admin")
        db.session.add(role)
        db.session.commit()
    else:
        role = Role.query.filter_by(name='admin').first()
    if User.query.filter_by().count() == 1:
        user = User.query.filter_by().first()
        user.roles = [role]
        db.session.commit()
    print("Setting up the app!")


application = DispatcherMiddleware(frontend_app, {
    '/api': api_app,
    '/restless': restless_app
})

if __name__ == "__main__":

    # Preform Database Upgrades Automatically :)
    command = '''
        alembic upgrade head
    '''
    Popen(command, shell=True)

    run_simple('0.0.0.0', 9360, application, use_reloader=True, use_debugger=True)
