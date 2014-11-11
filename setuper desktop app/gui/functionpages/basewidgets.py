#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class BaseToolButton(QtWidgets.QPushButton):
    """docstring for BaseButton"""

    def __init__(self, text="", parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.parent = parent
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setObjectName("FlatUIButton")
        self.setFlat(True)
        self.setFixedSize(60, 40)
        self.setText(text)



class BaseButton(QtWidgets.QPushButton):

    def __init__(self, button_id, parent=None):
        super(BaseButton, self).__init__(parent)
        self.parent = parent
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_id = button_id
        self.setObjectName(button_id)
        self.state = 0
        self.buttons = ['up', 'down']

        style = '''QPushButton{
            border-image: url(gui/skin/images/%s_%s.png);
        }'''%(self.button_id, self.buttons[self.state])
        self.setStyleSheet(style)

        self.pressed.connect(self.actionPress)
        self.released.connect(self.actionRelease)
        self.clicked.connect(self.actionclick)

    def setState(self, state):
        self.state = state
        style = '''QPushButton{
            border-image: url(gui/skin/images/%s_%s.png);
        }'''%(self.button_id, self.buttons[self.state])
        self.setStyleSheet(style)

    def mouseDoubleClickEvent(self, event):
        pass

    def actionPress(self):
        pass

    def actionRelease(self):
        pass

    def actionclick(self):
        self.state = not self.state
        style = '''QPushButton{
            border-image: url(gui/skin/images/%s_%s.png);
        }'''%(self.button_id, self.buttons[self.state])
        self.setStyleSheet(style)

    def buttonEventProto(self, data):
        pass



class BaseLabel(QtWidgets.QLabel):
    """docstring for BaseButton"""

    def __init__(self, text, parent=None):
        super(BaseLabel, self).__init__(parent)
        self.parent = parent
        self.setFixedSize(200, 40)
        self.setText(text)

class BaseLineEdit(QtWidgets.QLineEdit):
    """docstring for BaseButton"""

    def __init__(self, parent=None):
        super(BaseLineEdit, self).__init__(parent)
        self.parent = parent
        self.setMinimumSize(200, 36)
