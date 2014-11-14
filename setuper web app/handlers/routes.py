#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tornado.web
from joinhandler import JoinHandler
from loginhandler import LoginHandler, LogoutHandler
from indexhandler import IndexHandler
from sockethandler import SocketHandler
from producthandler import DesktopHandler, CliHandler
from uploadfilehandler import UploadFileHandler
from helphandler import HelpHandler, HelpCliHandler
from abouthandler import AboutHandler
from contacthandler import ContactHandler


from admin.adminhandler import AdminLoginHandler, AdminLogoutHandler
from admin.adminindexhandler import AdminIndexHandler


routes = [
    (r"/", IndexHandler),
    (r"/ws", SocketHandler),
    (r"/join/*", JoinHandler),
    (r"/login/*", LoginHandler),
    (r"/logout/*", LogoutHandler),
    (r"/upload", UploadFileHandler),
    (r"/desktop/*", DesktopHandler),
    (r"/cli/*", CliHandler),
    (r"/help/*", HelpHandler),
    (r"/help/cli/*", HelpCliHandler),
    (r"/about/*", AboutHandler),
    (r"/contact/*", ContactHandler),
    (r'/static', tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), "static")})
]

adminroutes = [
    (r"/admin/*", AdminIndexHandler),
    (r"/admin/login/*", AdminLoginHandler),
    (r"/admin/logout/*", AdminLogoutHandler)
]

routes.extend(adminroutes)
