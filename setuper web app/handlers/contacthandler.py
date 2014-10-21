#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class ContactHandler(BaseHandler):

    def get(self):
        print self.dbSession, '+++++++', self.current_user
        self.render("contact.html", title="Cloud Setuper")
