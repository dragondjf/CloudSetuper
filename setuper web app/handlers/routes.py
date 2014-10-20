#!/usr/bin/env python
# -*- coding: utf-8 -*-

from registerhandler import RegisterHandler
from loginhandler import LoginHandler
from indexhandler import IndexHandler
from uploadfilehandler import UploadFileHandler


routes = [
	(r"/", IndexHandler),
	(r"/join", RegisterHandler),
	(r"/login", LoginHandler),
	(r"/upload", UploadFileHandler),
]
