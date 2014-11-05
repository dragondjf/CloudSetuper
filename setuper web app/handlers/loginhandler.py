#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler
from models import User
import logging
import base64


class LoginHandler(BaseHandler):

    count = 0

    def get(self):
        self.render("login.html", title="Cloud Setuper Sign in", username=self.current_user)

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        user = {
                'username': username,
                'password': password
            }
        checkstatus = self.checkUser(user)
        if checkstatus['status']:
            self.set_secure_cookie("user", username)
            response = {
                'status': "success",
                'info': checkstatus['info']
            }
            self.count += 1
        else:
            response = {
                'status': "fail",
                'info': checkstatus['info']
            }
        self.write(response)

    def checkUser(self, user):
        col = User.getCollection()
        result = col.find_one({'username': user['username']})
        if result:
            if base64.decodestring(result['password']) == user['password']:
                return {
                    'status': True,
                    'info': "login success"
                }
            else:
                return {
                    'status': False,
                    'info': "The password is wrong, please check password."
                }
        else:
            return {
                'status': False,
                'info': "This user isn't exits, please check username."
            }


class LogoutHandler(BaseHandler):

    @authenticated
    def post(self):
        self.clear_cookie(self.get_current_user())
        LoginHandler.count -= 1
        # self.clear_all_cookies()
