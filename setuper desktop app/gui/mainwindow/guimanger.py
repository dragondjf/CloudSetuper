#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from PyQt5 import QtCore
from gui.functionpages.colorpopupframe import ColorPopupFrame
from .guiconfig import views
from ws4py.client.threadedclient import WebSocketClient
from dataBase import signal_DB


class EchoClient(WebSocketClient):
    
    def opened(self):
        # self.send("*" * i)
        pass

    def closed(self, code, reason):
        print(("Closed down", code, reason))

    def received_message(self, m):
        counts = json.loads(str(m))
        signal_DB.count_sin.emit(counts['allCount'])


class GuiManger(QtCore.QObject):

    """docstring for GuiManger"""

    def __init__(self, parent=None):
        super(GuiManger, self).__init__()
        self.parent = parent
        self.initConnect()
        self.initWebSocket()

    def initConnect(self):
        exitButton = views['NavgationBar'].buttons['Exit']
        exitButton.clicked.connect(views['MainWindow'].close)
        views['TitleBar'].skinButton.clicked.connect(self.changeBgColor)

    def changeBgColor(self):
        colorpopupframe = ColorPopupFrame(views['MainWindow'])
        colorpopupframe.show()

    def initWebSocket(self):
        try:
           ws = EchoClient('ws://106.186.19.60/ws', protocols=['http-only', 'chat'])
           ws.connect()
        except KeyboardInterrupt:
           ws.close()
