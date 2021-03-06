# -*- coding: utf-8 -*-
"""
    straply.helpers
    ~~~~~~~~~~~~~~~~

    straply helpers module
"""

import pkgutil
import importlib
import string
import random
import hashlib
import datetime

from threading import Thread
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

from flask import Blueprint
from flask.json import JSONEncoder as BaseJSONEncoder
from flask_mail import Message as Msg
from settings import ALLOWED_EXTENSIONS

from .core import mail


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async
def send_async_email(msg):
    from frontend import create_app
    with create_app().test_request_context():
        mail.send(msg)


def send_email(
        subject,
        recipients,
        sender='me@nickwoodhams.com',
        html_body=None,
        plain_body=None,
        reply_to=None,
        bcc=['nicholas.woodhams@gmail.com'],
        host=None,
        testmode=False):
        # Flask Mail Parameters
        # subject – email subject header
        # recipients – list of email addresses
        # body – plain text message
        # html – HTML message
        # sender – email sender address, or MAIL_DEFAULT_SENDER by default
        # cc – CC list
        # bcc – BCC list
        # attachments – list of Document instances
        # reply_to – reply-to address
        # date – send date
        # charset – message character set
        # extra_headers – A dictionary of additional headers for the message
    msg = Msg(
        subject=subject,
        recipients=recipients,
        body=dehtml(html_body) if not plain_body else plain_body,
        html=html_body,
        sender=sender,
        reply_to=reply_to,
        bcc=bcc)
    if testmode is True:
        msg.extra_headers = {"o:testmode": "yes"}
    else:
        send_async_email(msg)


class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


@async
def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


def firstname(full_name):
    try:
        return full_name.split(' ')[0]
    except:
        return full_name


# Return natural time
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"


def current_date():
    return datetime.datetime.utcnow


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def gravatar(email, size=80):
    hashresp = hashlib.md5(email).hexdigest()
    return '//www.gravatar.com/avatar/' + str(hashresp) + '?s=' + str(size)


def MD5(str):
    return hashlib.md5(str).hexdigest()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))


def nl2br(value):
        return value.replace('\n', '<br>\n')


def format_currency(value):
    if not value:
        return "$0.00"
    return "${:,.0f}".format(value)


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv
