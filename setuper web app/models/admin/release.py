#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from  models.basedocment import BaseDocment
from models.dbsession import connection

@connection.register
class Release(BaseDocment):

    __collection__ = 'releaseCol'
    __database__ = 'setuperDB'

    structure = {
        'softwarename': unicode,
        'softwareversion': unicode,
        'softwareauthor': unicode,
        'softwareurl': unicode,
        'releasenotes': unicode,
        'date_creation': datetime.datetime,
    }
    required_fields = ['softwarename', 'softwareurl', 'releasenotes']
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }
