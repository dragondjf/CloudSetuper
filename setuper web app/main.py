#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid

from handlers import routes
from models import dbSession

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = routes
        settings = dict(
            cookie_secret=str(uuid.uuid5(uuid.NAMESPACE_DNS, "cloud setuper")),
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            login_url = "/login",
            # xsrf_cookies=True,
            gzip=True,
            # debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.dbSession = dbSession


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
