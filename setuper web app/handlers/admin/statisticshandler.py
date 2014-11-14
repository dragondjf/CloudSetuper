#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado.web import authenticated, removeslash
from handlers.basehandlers import BaseHandler
import logging
import json


class StatisticsHandler(BaseHandler):

    role = "admin"

    @authenticated
    @removeslash
    def get(self):
        self.render("admin/statistics.html", title="Cloud Setuper", username=self.current_user)
