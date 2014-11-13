#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class HelpHandler(BaseHandler):

    def get(self):
        self.render("help_zh.html", title="Cloud Setuper", username=self.current_user)

class HelpCliHandler(BaseHandler):

    def get(self):
        self.render("helpcli_zh.html", title="Cloud Setuper", username=self.current_user)
