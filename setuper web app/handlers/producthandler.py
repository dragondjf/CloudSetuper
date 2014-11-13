#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class DesktopHandler(BaseHandler):

    def get(self):
        self.render("desktop.html", title="Cloud Setuper", username=self.current_user)

class CliHandler(BaseHandler):

    def get(self):
        self.render("cli.html", title="Cloud Setuper", username=self.current_user)
