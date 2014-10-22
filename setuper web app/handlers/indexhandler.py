#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class IndexHandler(BaseHandler):

    @authenticated
    def get(self):
        if not self.current_user:  
            self.redirect("/login")  
            return
        self.render("index.html", title="Cloud Setuper", username=self.current_user)

    def post(self):
        softwarename = self.get_argument("softwarename", "")
        softwareauthor = self.get_argument("softwareauthor", "")
        softwareemail = self.get_argument("softwareemail", "")
        softwarecompany = self.get_argument("softwarecompany", "")
        main_progressbar_on = self.get_argument("main_progressbar_on", "")
        taskbar_progressbar_on = self.get_argument("taskbar_progressbar_on", "")
        desktoplink_on = self.get_argument("desktoplink_on", "")

        software = {
            'softwarename': softwarename,
            'softwareauthor': softwareauthor,
            'softwareemail': softwareemail,
            'softwarecompany': softwarecompany,
            'main_progressbar_on': main_progressbar_on,
            'taskbar_progressbar_on': taskbar_progressbar_on,
            'desktoplink_on': desktoplink_on
        }
        print software
        flag = self.onesetup(software)
        response = {
            'status': "success"
        }
        self.write(response)

    def onesetup(self, software):
    	print "onesetup==================="
