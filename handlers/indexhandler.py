#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basehandlers import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        print self.dbSession
        self.render("index.html", title="Cloud Setuper")
