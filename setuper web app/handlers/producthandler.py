#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated, removeslash
from basehandlers import BaseHandler
from models.admin.release import Release 


class DesktopHandler(BaseHandler):

    @removeslash
    def get(self):
        result = self.getLastestReleaseInfo()
        self.render("desktop.html", title="Cloud Setuper", release=result, username=self.current_user)

    @classmethod
    def getLastestReleaseInfo(cls):
        col = Release.getCollection()
        result = list(col.find({'softwarename': "CloudSetuper Desktop"}))
        if len(result) > 0:
            return result[-1]
        else:
            return None

class CliHandler(BaseHandler):

    @removeslash
    def get(self):
        result = self.getLastestReleaseInfo()
        self.render("cli.html", title="Cloud Setuper", release=result, username=self.current_user)

    @classmethod
    def getLastestReleaseInfo(cls):
        col = Release.getCollection()
        result = list(col.find({'softwarename': "CloudSetuper CLI"}))
        if len(result) > 0:
            return result[-1]
        else:
            return None


class DesktopReleaseHandler(BaseHandler):

    @removeslash
    def get(self):
        results = self.getReleaseInfo()
        print results
        self.render("desktoprelease.html", title="Cloud Setuper", releases=results ,username=self.current_user)

    @classmethod
    def getReleaseInfo(cls):
        col = Release.getCollection()
        result = list(col.find({'softwarename': "CloudSetuper Desktop"}))
        return result[::-1]


class CLIReleaseHandler(BaseHandler):

    @removeslash
    def get(self):
        results = self.getReleaseInfo()
        self.render("clirelease.html", title="Cloud Setuper", releases=results, username=self.current_user)

    @classmethod
    def getReleaseInfo(cls):
        col = Release.getCollection()
        result = list(col.find({'softwarename': "CloudSetuper CLI"}))
        return result[::-1]

