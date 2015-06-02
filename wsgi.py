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

application = DispatcherMiddleware(frontend.create_app(), {
    '/api': api.create_app(),
    '/restless': restless.create_app()
})

if __name__ == "__main__":

    # Preform Database Upgrades Automatically :)
    command = '''
        alembic upgrade head
    '''
    Popen(command, shell=True)

    run_simple('0.0.0.0', 9360, application, use_reloader=True, use_debugger=True)
