#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.websocket
from loginhandler import LoginHandler
from joinhandler import JoinHandler
from indexhandler import IndexHandler
import json

clients = {}

class SocketHandler(tornado.websocket.WebSocketHandler):

    def open(self, *args):
        self.id = id(self)
        self.stream.set_nodelay(True)
        clients[self.id] = self

        IndexHandler.getCount(self.current_user) 

    def on_message(self, message):
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        pass

    def sendMessage(self, message):
        self.write_message(json.dumps(message))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]

    def initialize(self):
        ''' Setup sessions, etc '''
        self.session = None
        self.connection = self.application.connection

    def get_current_user(self):
        ''' Get current user object from database '''
        return self.get_secure_cookie("user")
