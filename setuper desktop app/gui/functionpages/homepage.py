#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
from .webkitbasepage import WebkitBasePage
from .basewidgets import *

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
        self.files = []

    def initUI(self):
        self.setFixedHeight(200)
        self.browseButton = BaseToolButton(self.tr("Browser"), self)
        self.browseButton.setObjectName("FlatUIButton")
        self.browseButton.move(120, 80)

    def initConnect(self):
        self.browseButton.clicked.connect(self.uploadfiles)

    def uploadfiles(self):
        files = QtWidgets.QFileDialog.getOpenFileNames(
                        self,
                        "Select 7z or image files to open",
                        os.getcwd(),
                        "files (*.7z *.png *.bmp *.jpg)")[0]
        self.files += files
        print(self.files)
        files = [os.path.basename(f) for f in self.files[::-1]]
        self.fileListSignal.emit(files)


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
        self.parent.browerPage.files.pop(row)

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
        self.clearSelf()
        for t in items:
            self.appItem(t)

    def clearSelf(self):
        for i in range(self.rowCount() + 1):
            self.removeRow(0)


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


class SetuperPage(QtWidgets.QFrame):

    viewID = "SetuperPage"

    keys = [
        "softwarename", 
        "outputfoldername", 
        "exename", 
        "desktoplinkname", 
        "softwareversion", 
        "softwareauthor",
        "softwareemail", 
        "softwarecompany"
    ]

    @collectView
    def __init__(self, parent=None):
        super(SetuperPage, self).__init__(parent)
        self.setObjectName("SetuperPage")
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.setFixedWidth(420)
        mainLayout = QtWidgets.QGridLayout()

        softwarenameLabel = BaseLabel(self.tr("Software name:"))
        self.softwarenameLineEdit = BaseLineEdit()

        outputfoldernameLabel = BaseLabel(self.tr("Outputfolder name:"))
        self.outputfoldernameLineEdit = BaseLineEdit()

        exenameLabel = BaseLabel(self.tr("Exe name:"))
        self.exenameLineEdit = BaseLineEdit()

        desktoplinknameLabel = BaseLabel(self.tr("Desktoplink name:"))
        self.desktoplinkLineEdit = BaseLineEdit()

        softwareversionLabel = BaseLabel(self.tr("Software version:"))
        self.softwareversionLineEdit = BaseLineEdit()

        softwareauthorLabel = BaseLabel(self.tr("Software author:"))
        self.softwareauthorLineEdit = BaseLineEdit()

        softwareemailLabel = BaseLabel(self.tr("Software email:"))
        self.softwareemailLineEdit = BaseLineEdit()

        softwarecompanyLabel = BaseLabel(self.tr("Software company:"))
        self.softwarecompanyLineEdit = BaseLineEdit()

        desktoplinkLabel = BaseLabel(self.tr("Desktop link or not:"))
        desktoplinkButton = BaseButton("switch")
        desktoplinkButton.setFixedSize(90, 33)

        languageLabel = BaseLabel(self.tr("Language:"))
        self.languageCombox = QtWidgets.QComboBox()
        self.languageCombox.setFixedHeight(36)
        self.languageCombox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.languageCombox.addItem("en")
        self.languageCombox.addItem("zh_CN")
        self.languageCombox.addItem("zh_TW")


        themeLabel = BaseLabel(self.tr("Theme color:"))

        templateLabel = BaseLabel(self.tr("Template:"))

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(softwarenameLabel, 0, 0)
        mainLayout.addWidget(self.softwarenameLineEdit, 0, 1)

        mainLayout.addWidget(outputfoldernameLabel, 1, 0)
        mainLayout.addWidget(self.outputfoldernameLineEdit, 1, 1)

        mainLayout.addWidget(exenameLabel, 2, 0)
        mainLayout.addWidget(self.exenameLineEdit, 2, 1)

        mainLayout.addWidget(desktoplinknameLabel, 3, 0)
        mainLayout.addWidget(self.desktoplinkLineEdit, 3, 1)

        mainLayout.addWidget(softwareversionLabel, 4, 0)
        mainLayout.addWidget(self.softwareversionLineEdit, 4, 1)

        mainLayout.addWidget(softwareauthorLabel, 5, 0)
        mainLayout.addWidget(self.softwareauthorLineEdit, 5, 1)

        mainLayout.addWidget(softwareemailLabel, 6, 0)
        mainLayout.addWidget(self.softwareemailLineEdit, 6, 1)

        mainLayout.addWidget(softwarecompanyLabel, 7, 0)
        mainLayout.addWidget(self.softwarecompanyLineEdit, 7, 1)

        mainLayout.addWidget(desktoplinkLabel, 8, 0)
        mainLayout.addWidget(desktoplinkButton, 8, 1)

        mainLayout.addWidget(languageLabel, 9, 0)
        mainLayout.addWidget(self.languageCombox, 9, 1)

        mainLayout.addWidget(themeLabel, 10, 0)

        mainLayout.addWidget(templateLabel, 11, 0)

        

        mainLayout.setSpacing(1)
        mainLayout.setContentsMargins(20, 10, 30, 0)
        mainLayout.setRowStretch(11, 1)

        self.setLayout(mainLayout)

    def initConnect(self):
        self.softwarenameLineEdit.textChanged.connect(self.outputfoldernameLineEdit.setText)
        self.softwarenameLineEdit.textChanged.connect(self.exenameLineEdit.setText)
        self.softwarenameLineEdit.textChanged.connect(self.desktoplinkLineEdit.setText)

    def getFormData(self):
        return {
            "softwarename": self.softwarecompanyLineEdit.text(),
            "outputfoldername": self.outputfoldernameLineEdit.text(),
            "exename": self.exenameLineEdit.text(),
            "desktoplinkname": self.desktoplinkLineEdit.text(),
            "softwareversion": self.softwareversionLineEdit.text(),
            "softwareauthor": self.softwareauthorLineEdit.text(),
            "softwareemail": self.softwarenameLineEdit.text(),
            "softwarecompany": self.softwarecompanyLineEdit.text()
        }



class BuildPage(QtWidgets.QFrame):

    viewID = "BuildPage"

    @collectView
    def __init__(self, parent=None):
        super(BuildPage, self).__init__(parent)
        self.setObjectName("BuildPage")
        self.parent = parent
        self.initData()
        self.initUI()

    def initData(self):
        pass

    def initUI(self):
        self.buildButton = BaseToolButton(self.tr("Build"))
        self.buildButton.setObjectName("FlatUIButton")
        self.buildButton.setFixedWidth(200)
        self.exportButton = BaseToolButton(self.tr("Export"))
        self.exportButton.setObjectName("FlatUIButton")
        self.exportButton.setFixedWidth(200)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addWidget(self.buildButton)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.exportButton)

        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)



class HomePage(QtWidgets.QFrame):

    viewID = "HomePage"

    @collectView
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.setObjectName("HomePage")
        self.parent = parent
        self.initData()
        self.initUI()
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.uploadPage = UploadPage(self)
        self.setuperPage = SetuperPage(self)
        self.buildPage = BuildPage(self)
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.uploadPage)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.setuperPage)
        mainLayout.addWidget(self.buildPage)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(5, 0, 0, 0)
        self.setLayout(mainLayout)

    def initConnect(self):
        self.buildPage.buildButton.clicked.connect(self.build)

    def build(self):
        software = self.setuperPage.getFormData()
        
        software['files'] = files
        fd = open(os.sep.join([softwarefolder, 'package.json']), 'wb')
        fd.write(json.dumps(software, indent=4))
        fd.close()
