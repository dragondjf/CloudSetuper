#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        httpfile = self.request.files['upl'][0]
        if httpfile:
            print httpfile.keys()
            print httpfile['content_type']
            print httpfile['filename']
            fd = open("static/files/%s" % httpfile['filename'], "w")
            fd.write(httpfile['body'])
            fd.close()
