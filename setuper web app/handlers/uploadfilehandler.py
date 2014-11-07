#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado.web import authenticated
from basehandlers import BaseHandler


class UploadFileHandler(BaseHandler):

    @authenticated
    def get(self):
        if not self.current_user:  
            self.redirect("/login")  
            return
        self.render("uploadfile.html", title="Cloud Setuper", username=self.current_user)

    @authenticated
    def post(self):
        if self.request.files:
            for f in self.request.files['upl']:
                httpfile = f
                if httpfile:
                    pwd = os.path.dirname(os.path.dirname(__file__))
                    path = os.sep.join([pwd, 'static', 'files'])
                    if not os.path.exists(path):
                        os.mkdir(path)
                    fd = open("static/files/%s" % httpfile['filename'], "wb")
                    fd.write(httpfile['body'])
                    fd.close()

    @authenticated
    def delete(self):
        filename = self.get_argument("filename", "")
        path = os.sep.join([os.getcwd(), 'static', 'files', filename])
        if os.path.exists(path):
            os.remove(path)
            response = {
                "status": "success",
            }
        else:
            response = {
                "status": "fail",
            }
        self.write(response)
