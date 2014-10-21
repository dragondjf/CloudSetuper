#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class AboutHandler(BaseHandler):

    def get(self):
        print self.dbSession, '+++++++', self.current_user
        self.render("about.html", title="Cloud Setuper")
