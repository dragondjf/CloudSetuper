#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class HelpHandler(BaseHandler):

    def get(self):
        self.render("help.html", title="Cloud Setuper")
