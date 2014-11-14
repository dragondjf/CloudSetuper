#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated, removeslash
from basehandlers import BaseHandler


class AboutHandler(BaseHandler):

    @removeslash
    def get(self):
        self.render("about.html", title="Cloud Setuper", username=self.current_user)
