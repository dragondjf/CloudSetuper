#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from handlers.basehandlers import BaseHandler

adminusers = [
    {
        'username': 'admin',
        'password': 'admin' 
    }
]


class AdminLoginHandler(BaseHandler):

    role = "admin"

    def get(self):
        if self.current_user:
            self.redirect('/admin')
        self.render("admin/login.html", title="Cloud Setuper", username=self.current_user)

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        user = {
                'username': username,
                'password': password
            }
        checkstatus = self.checkUser(user)
        if checkstatus['status']:
            self.set_secure_cookie(self.role, username)
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

    def checkUser(self, user):
        if user in adminusers:
            return {
                'status': True,
                'info': "login success"
            }
        else:
            return {
                'status': False,
                'info': "please check username or password."
            }

class AdminLogoutHandler(BaseHandler):

    role = "admin"

    @authenticated
    def post(self):
        self.clear_cookie(self.get_current_user())
