# -*- coding: utf-8 -*-
"""
    straply
    ~~~~~~~~
    straply user service
"""


from ..core import Service
from .models import User

#create services
class UserService(Service):
    __model__ = User
