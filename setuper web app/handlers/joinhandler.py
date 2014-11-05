#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basehandlers import BaseHandler
from models import User
import logging
import base64


class JoinHandler(BaseHandler):

    count = 0

    def get(self):
        self.render("join.html", title="Join Cloud Setuper", username=self.current_user)

    def post(self):
        username = self.get_argument("username", "")
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")

        user = {
                'username': username,
                'email': email,
                'password': base64.encodestring(password)
            }
        checkstatus = self.checkUser(user)
        if checkstatus['status']:
            objId = self.saveUser2DB(user)
            logging.info(objId)
            self.set_secure_cookie("user", username)
            response = {
                'status': "success",
                'info': "register success"
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
        userCount = col.find({'username': user['username']}).count()
        emailCount = col.find({'email': user['email']}).count()
        if userCount == 0 and emailCount == 0:
            return {
                'status': True,
                'info': "new user"
            }
        elif userCount !=0:
            return {
                'status': False,
                'info': "This user has been registered"
            }
        elif emailCount != 0:
            return {
                'status': False,
                'info': "This email has been registered"
            }

    def saveUser2DB(self, dictobj):
        user = self.connection.User()
        objId = user.loadFromDict(dictobj)
        return objId
