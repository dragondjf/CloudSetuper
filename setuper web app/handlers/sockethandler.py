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

    def on_message(self, message):
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        counts = {
        	'join': JoinHandler.count,
        	'online': LoginHandler.count,
        	'build': IndexHandler.count
        }
        self.write_message(json.dumps(counts))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]
