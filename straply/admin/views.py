
# Views get initiated in frontend/__init__.property

from pprint import pprint
from datetime import date, timedelta

from flask import make_response, request, current_app, flash, redirect, \
    url_for, render_template, abort
from flask.ext.admin import Admin, BaseView, AdminIndexView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.sqla.form import InlineModelConverter, get_form
from flask.ext.admin.model.template import macro
from flask_security import current_user
from sqlalchemy.sql import func
from sqlalchemy.orm import object_mapper


from ..core import db
from ..models import User
from ..forms import createUserExtendedForm


class AdminModel(ModelView):

    def is_accessible(self):
        return True  # comment this line out after adding admin role
        return current_user.has_role('admin')


class UserView(AdminModel):
    # Disable model creation
    can_create = True

    # Override displayed fields
    column_list = ('name', 'email')
    column_searchable_list = ('name', 'email',)
    # column_filters = ('posted_at', 'user.id', 'user.name', 'user.username',
    #                   'user.email')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UserView, self).__init__(User, session, **kwargs)


class MyHomeView(AdminIndexView):

    @expose('/')
    def index(self):
        # if current_user.is_anonymous():
        #     return redirect('/login?next=%2fadmin')
        # elif not current_user.has_role('admin'):
        #     return abort(401)

        # Users
        users = User.query.filter_by().all()

        return self.render(
            'admin/index.html',
            users=users)
