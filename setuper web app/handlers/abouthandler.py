#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class AboutHandler(BaseHandler):

    def get(self):
        self.render("about.html", title="Cloud Setuper", username=self.current_user)
