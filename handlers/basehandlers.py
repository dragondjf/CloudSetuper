#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def initialize(self):
        ''' Setup sessions, etc '''
        self.session = None
        self.dbSession = self.application.dbSession

    def get_current_user(self):
        ''' Get current user object from database '''
        if self.session is not None:
            try:
                return "dragondjf"
            except KeyError:
                logging.exception("Malformed session: %r" % self.session)
            except:
                logging.exception("Failed call to get_current_user()")
        return None
