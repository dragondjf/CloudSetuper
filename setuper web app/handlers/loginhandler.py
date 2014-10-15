#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basehandlers import BaseHandler

class LoginHandler(BaseHandler):

    def get(self):
        self.render("login.html", title="Cloud Setuper Sign in")


    def post(self):
        name = self.get_argument("name", "")
        password = self.get_argument("password", "")
        user = {
                'name': name,
                'password': password
            }

        flag = self.checkUser(user)
        if flag:
            self.set_secure_cookie("user", name)
            self.redirect("/")
        else:
            pass

    def checkUser(self, user):
        return True
