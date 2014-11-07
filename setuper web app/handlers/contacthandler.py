#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler
import logging


class ContactHandler(BaseHandler):

    def get(self):
        logging.info(self.connection, '+++++++', self.current_user)
        self.render("contact.html", title="Cloud Setuper", username=self.current_user)
