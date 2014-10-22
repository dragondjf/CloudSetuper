#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basehandlers import BaseHandler

class LoginHandler(BaseHandler):

    def get(self):
        self.render("login.html", title="Cloud Setuper Sign in")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        user = {
                'username': username,
                'password': password
            }
        print user
        flag = self.checkUser(user)
        if flag:
            self.set_secure_cookie("user", username)
            response = {
                'status': "success"
            }
            self.write(response)

    def checkUser(self, user):
        col = self.connection['setuperDB']['userCol']
        return True
