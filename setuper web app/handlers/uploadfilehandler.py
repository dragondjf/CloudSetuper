#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado.web import authenticated
from basehandlers import BaseHandler


class UploadFileHandler(BaseHandler):

    @authenticated
    def get(self):
        print self.dbSession, '+++++++', self.current_user
        if not self.current_user:  
            self.redirect("/login")  
            return
        self.render("uploadfile.html", title="Cloud Setuper")

    @authenticated
    def post(self):
        if self.request.files:
            for f in self.request.files['upl']:
                httpfile = f
                if httpfile:
                    path = os.sep.join([os.getcwd(), 'static', 'files'])
                    if not os.path.exists(path):
                        os.mkdir(path)
                    fd = open("static/files/%s" % httpfile['filename'], "wb")
                    fd.write(httpfile['body'])
                    fd.close()
