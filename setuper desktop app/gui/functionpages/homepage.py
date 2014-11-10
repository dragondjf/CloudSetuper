#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
from .webkitbasepage import WebkitBasePage


class BaseToolButton(QtWidgets.QPushButton):
    """docstring for BaseButton"""

    def __init__(self, text, parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.parent = parent
        self.setFlat(True)
        self.setFixedSize(60, 40)
        self.setText(text)

class BrowsePage(QtWidgets.QFrame):

    viewID = "BrowsePage"


    fileListSignal = QtCore.pyqtSignal(list)

    @collectView
    def __init__(self, parent=None):
        super(BrowsePage, self).__init__(parent)
        self.setObjectName("BrowsePage")
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedHeight(200)
        self.browseButton = BaseToolButton(self.tr("Browser"), self)
        self.browseButton.setObjectName("FlatUIButton")
        self.browseButton.move(120, 80)

    def initConnect(self):
        self.browseButton.clicked.connect(self.uploadfiles)

    def uploadfiles(self):
        self.files = QtWidgets.QFileDialog.getOpenFileNames(
                        self,
                        "Select 7z or image files to open",
                        os.getcwd(),
                        "files (*.7z *.png *.bmp *.jpg)")
        files = [os.path.basename(f) for f in self.files[0]]
        self.fileListSignal.emit(files)


class UploadPage(QtWidgets.QFrame):

    viewID = "UploadPage"

    @collectView
    def __init__(self, parent=None):
        super(UploadPage, self).__init__(parent)
        self.setObjectName("UploadPage")
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedWidth(300)
        self.browerPage = BrowsePage(self)
        self.fileListPage = FilesListPage(self)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.browerPage)
        mainLayout.addWidget(self.fileListPage)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

    def initConnect(self):
        self.browerPage.fileListSignal.connect(self.fileListPage.appItems)


class FilesListPage(QtWidgets.QTableWidget):

    viewID = "FilesListPage"

    @collectView
    def __init__(self, parent=None):
        super(FilesListPage, self).__init__(parent)
        self.parent = parent
        self.setObjectName("FilesListPage")
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setEditTriggers(self.NoEditTriggers)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setShowGrid(True)
        self.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.setColumnCount(2)
        self.setColumnWidth(0, 260)
        self.setColumnWidth(1, 40)

    def initConnect(self):
        self.cellDoubleClicked.connect(self.removeItem)

    def removeItem(self, row, count):
        self.removeRow(row)

    def appItem(self, t):
        self.insertRow(0)
        for i in range(0, self.columnCount()):
            if i == 0:
                item = QtWidgets.QTableWidgetItem(t)
            if i == 1:
                item = QtWidgets.QTableWidgetItem('x')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.setItem(0, i, item)

    def appItems(self, items):
        for t in items:
            self.appItem(t)


class SetuperPage(QtWidgets.QFrame):

    viewID = "SetuperPage"

    @collectView
    def __init__(self, parent=None):
        super(SetuperPage, self).__init__(parent)
        self.setObjectName("SetuperPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedWidth(600)



class HomePage(QtWidgets.QFrame):

    viewID = "HomePage"

    @collectView
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.setObjectName("HomePage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        uploadPage = UploadPage(self)
        setuperPage = SetuperPage(self)
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(uploadPage)
        mainLayout.addWidget(setuperPage)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(5, 0, 0, 0)
        self.setLayout(mainLayout)
