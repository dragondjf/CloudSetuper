#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado.web import authenticated, removeslash
from handlers.basehandlers import BaseHandler
from models import Release
import logging
import json


class ReleaseHandler(BaseHandler):

    role = "admin"

    @authenticated
    @removeslash
    def get(self):
        self.render("admin/release.html", title="Cloud Setuper", username=self.current_user)

    @authenticated
    def post(self):
        softwarename = self.get_argument("softwarename", "")
        softwareversion = self.get_argument("softwareversion", "")
        softwareauthor = self.get_argument("softwareauthor", "")
        softwareurl = self.get_argument("softwareurl", "")
        releasenotes = self.get_argument("releasenotes", "")

        releaseInfo = {
            'softwarename': softwarename,
            'softwareversion': softwareversion,
            'softwareauthor': softwareauthor,
            'softwareurl': softwareurl,
            'releasenotes': releasenotes
        }
        checkstatus = self.checkReleaseInfo(releaseInfo)
        if checkstatus['status']:
            objId = self.saveRelease2DB(releaseInfo)
            logging.info(objId)
            response = {
                'status': "success",
                'info': checkstatus['info']
            }
        else:
            response = {
                'status': "fail",
                'info': checkstatus['info']
            }
        self.write(response)

    def checkReleaseInfo(self, obj):
        return {
            'status': True,
            'info': "new release"
        }

    def saveRelease2DB(self, obj):
        release = self.connection.Release()
        objId = release.loadFromDict(obj)
        return objId
