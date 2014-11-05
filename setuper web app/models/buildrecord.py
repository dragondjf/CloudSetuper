#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basedocment import BaseDocment
import datetime
from dbsession import connection

@connection.register
class BuildRecord(BaseDocment):

    __collection__ = 'buildRecordCol'
    __database__ = 'setuperDB'

    structure = {
        'username': unicode,
        'count': int,
        'date_creation': datetime.datetime,
    }
    required_fields = ['username', 'count']
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }


@connection.register
class BuildCount(BaseDocment):

    __collection__ = 'buildCountCol'
    __database__ = 'setuperDB'

    structure = {
        'count': int,
        'date_creation': datetime.datetime,
    }
    required_fields = ['count']
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }
