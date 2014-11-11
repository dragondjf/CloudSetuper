#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class SignalDB(QtCore.QObject):

    count_sin = QtCore.pyqtSignal(int)

    def __init__(self):
        super(SignalDB, self).__init__()

signal_DB = SignalDB()
