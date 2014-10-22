#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def initialize(self):
        ''' Setup sessions, etc '''
        self.session = None
        self.connection = self.application.connection

    def get_current_user(self):
        ''' Get current user object from database '''
        return self.get_secure_cookie("user")
