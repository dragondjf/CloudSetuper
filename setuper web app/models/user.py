#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basedocment import BaseDocment
import datetime
from dbsession import connection

@connection.register
class User(BaseDocment):

    __collection__ = 'userCol'
    __database__ = 'setuperDB'

    structure = {
        'username': unicode,
        'email': unicode,
        'password': unicode,
        'date_creation': datetime.datetime,
    }
    required_fields = ['username', 'email', 'password']
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }
