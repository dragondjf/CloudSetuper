#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class IndexHandler(BaseHandler):

    @authenticated
    def get(self):
        print self.dbSession, '+++++++', self.current_user
        if not self.current_user:  
            self.redirect("/login")  
            return  
        self.render("index.html", title="Cloud Setuper")
        # self.set_status(200)
