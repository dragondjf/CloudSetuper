#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    role = "user"

    def initialize(self):
        ''' Setup sessions, etc '''
        self.session = None
        self.connection = self.application.connection

    def get_current_user(self):
        ''' Get current user object from database '''
        return self.get_secure_cookie(self.role)

    def get_login_url(self):
        if self.role == "user":
            return super(BaseHandler, self).get_login_url()
        elif self.role == "admin":
            return "/admin/login"
