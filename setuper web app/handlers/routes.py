#!/usr/bin/env python
# -*- coding: utf-8 -*-

from joinhandler import JoinHandler
from loginhandler import LoginHandler, LogoutHandler
from indexhandler import IndexHandler
from uploadfilehandler import UploadFileHandler
from abouthandler import AboutHandler
from contacthandler import ContactHandler
routes = [
    (r"/", IndexHandler),
    (r"/join", JoinHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/upload", UploadFileHandler),
    (r"/about", AboutHandler),
    (r"/contact", ContactHandler)
]
