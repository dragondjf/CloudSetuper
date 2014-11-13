#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.wsgi
import os.path
import uuid
import wsgiref
import wsgiref.simple_server

from handlers import routes
from models import connection

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)
define("server", default='tornado', help="run on the given port", type=str)


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
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.connection = connection


def main():
    tornado.options.parse_command_line()
    app = Application()
    if options.server == "tornado":
        logging.info("Server is %s" % options.server)
        app.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    elif options.server == "wsgiref":
        logging.info("Server is %s" % options.server)
        wsgi_app = tornado.wsgi.WSGIAdapter(app)
        server = wsgiref.simple_server.make_server('', options.port, wsgi_app)
        server.serve_forever()


if __name__ == "__main__":
    main()
