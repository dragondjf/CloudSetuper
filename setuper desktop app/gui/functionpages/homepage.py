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

    def __init__(self, text="", parent=None):
        super(BaseToolButton, self).__init__(parent)
        self.parent = parent
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
        self.setFixedSize(200, 36)


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

    keys = [
        "software-name", 
        "outputfolder-name", 
        "exe-name", 
        "desktoplink-name", 
        "software-version", 
        "software-author",
        "software-email", 
        "software-company"
    ]

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
        self.setFixedWidth(420)
        mainLayout = QtWidgets.QGridLayout()

        softwarenameLabel = BaseLabel(self.tr("Software name:"))
        softwarenameLineEdit = BaseLineEdit()

        outputfoldernameLabel = BaseLabel(self.tr("Outputfolder name:"))
        outputfoldernameLineEdit = BaseLineEdit()

        exenameLabel = BaseLabel(self.tr("Exe name:"))
        exenameLineEdit = BaseLineEdit()

        desktoplinknameLabel = BaseLabel(self.tr("Desktoplink name:"))
        desktoplinkLineEdit = BaseLineEdit()

        softwareversionLabel = BaseLabel(self.tr("Software version:"))
        softwareversionLineEdit = BaseLineEdit()

        softwareauthorLabel = BaseLabel(self.tr("Software author:"))
        softwareauthorLineEdit = BaseLineEdit()

        softwareemailLabel = BaseLabel(self.tr("Software email:"))
        softwareemailLineEdit = BaseLineEdit()

        softwarecompanyLabel = BaseLabel(self.tr("Software company:"))
        softwarecompanyLineEdit = BaseLineEdit()

        desktoplinkLabel = BaseLabel(self.tr("Desktop link or not:"))
        desktoplinkButton = BaseButton("switch")
        desktoplinkButton.setFixedSize(90, 33)

        languageLabel = BaseLabel(self.tr("Language:"))
        languageCombox = QtWidgets.QComboBox()
        languageCombox.setFixedHeight(36)
        languageCombox.setFocusPolicy(QtCore.Qt.NoFocus)
        languageCombox.addItem("en")
        languageCombox.addItem("zh_CN")
        languageCombox.addItem("zh_TW")


        themeLabel = BaseLabel(self.tr("Theme color:"))

        templateLabel = BaseLabel(self.tr("Template:"))

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(softwarenameLabel, 0, 0)
        mainLayout.addWidget(softwarenameLineEdit, 0, 1)

        mainLayout.addWidget(outputfoldernameLabel, 1, 0)
        mainLayout.addWidget(outputfoldernameLineEdit, 1, 1)

        mainLayout.addWidget(exenameLabel, 2, 0)
        mainLayout.addWidget(exenameLineEdit, 2, 1)

        mainLayout.addWidget(desktoplinknameLabel, 3, 0)
        mainLayout.addWidget(desktoplinkLineEdit, 3, 1)

        mainLayout.addWidget(softwareversionLabel, 4, 0)
        mainLayout.addWidget(softwareversionLineEdit, 4, 1)

        mainLayout.addWidget(softwareauthorLabel, 5, 0)
        mainLayout.addWidget(softwareauthorLineEdit, 5, 1)

        mainLayout.addWidget(softwareemailLabel, 6, 0)
        mainLayout.addWidget(softwareemailLineEdit, 6, 1)

        mainLayout.addWidget(softwarecompanyLabel, 7, 0)
        mainLayout.addWidget(softwarecompanyLineEdit, 7, 1)

        mainLayout.addWidget(desktoplinkLabel, 8, 0)
        mainLayout.addWidget(desktoplinkButton, 8, 1)

        mainLayout.addWidget(languageLabel, 9, 0)
        mainLayout.addWidget(languageCombox, 9, 1)

        mainLayout.addWidget(themeLabel, 10, 0)

        mainLayout.addWidget(templateLabel, 11, 0)

        

        mainLayout.setSpacing(1)
        mainLayout.setContentsMargins(20, 10, 30, 0)
        mainLayout.setRowStretch(11, 1)

        self.setLayout(mainLayout)






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
        self.downloadButton = BaseToolButton(self.tr("DownLoad"))
        self.downloadButton.setObjectName("FlatUIButton")
        self.downloadButton.setFixedWidth(200)
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addStretch()
        mainLayout.addWidget(self.buildButton)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.downloadButton)

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

    def initData(self):
        pass

    def initUI(self):
        uploadPage = UploadPage(self)
        setuperPage = SetuperPage(self)
        buildPage = BuildPage(self)
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(uploadPage)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(setuperPage)
        mainLayout.addWidget(buildPage)
        mainLayout.addStretch()
        mainLayout.setContentsMargins(5, 0, 0, 0)
        self.setLayout(mainLayout)
