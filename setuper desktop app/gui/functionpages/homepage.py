#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from gui.mainwindow import collectView
from gui.mainwindow.guimanger import GuiManger
from .basewidgets import *
from .installcopy import generateConfig, generateExe


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
        packgeJsonPath = os.sep.join(['tools', 'package', 'package.json'])
        if os.path.exists(packgeJsonPath):
            fd = open(packgeJsonPath, 'r',encoding='utf8')
            self.software = json.load(fd)
            fd.close()
        else:
            self.software = {
                "softwarename": "",
                "outputfoldername": "", 
                "exename": "", 
                "desktoplinkname": "", 
                "softwareversion": "", 
                "softwareauthor": "",
                "softwareemail": "", 
                "softwarecompany": ""
            }

        self.color = "0x483d35"

    def initUI(self):
        self.setMinimumWidth(420)
        mainLayout = QtWidgets.QGridLayout()

        softwarenameLabel = BaseLabel(self.tr("Software name:"))
        self.softwarenameLineEdit = BaseLineEdit(self.software["softwarename"])

        outputfoldernameLabel = BaseLabel(self.tr("Outputfolder name:"))
        self.outputfoldernameLineEdit = BaseLineEdit(self.software["outputfoldername"])

        exenameLabel = BaseLabel(self.tr("Exe name:"))
        self.exenameLineEdit = BaseLineEdit(self.software["exename"])

        desktoplinknameLabel = BaseLabel(self.tr("Desktoplink name:"))
        self.desktoplinkLineEdit = BaseLineEdit(self.software["desktoplinkname"])

        softwareversionLabel = BaseLabel(self.tr("Software version:"))
        self.softwareversionLineEdit = BaseLineEdit(self.software["softwareversion"])

        softwareauthorLabel = BaseLabel(self.tr("Software author:"))
        self.softwareauthorLineEdit = BaseLineEdit(self.software["softwareauthor"])

        softwareemailLabel = BaseLabel(self.tr("Software email:"))
        self.softwareemailLineEdit = BaseLineEdit(self.software["softwareemail"])

        softwarecompanyLabel = BaseLabel(self.tr("Software company:"))
        self.softwarecompanyLineEdit = BaseLineEdit(self.software["softwarecompany"])

        desktoplinkLabel = BaseLabel(self.tr("Desktop link or not:"))
        self.desktoplinkButton = BaseButton("switch")
        self.desktoplinkButton.setFixedSize(90, 33)

        languageLabel = BaseLabel(self.tr("Language:"))
        self.languageCombox = QtWidgets.QComboBox()
        self.languageCombox.setFixedHeight(36)
        self.languageCombox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.languageCombox.addItem("en")
        self.languageCombox.addItem("zh_CN")
        self.languageCombox.addItem("zh_TW")


        themeLabel = BaseLabel(self.tr("Theme color:"))
        self.customColorButton = QtWidgets.QPushButton(self.tr(""))
        self.customColorButton.setFlat(True)
        self.customColorButton.setFixedSize(40, 40)
        self.customColorButton.setStyleSheet(self.colorqss("#353d48"))

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
        mainLayout.addWidget(self.desktoplinkButton, 8, 1)

        mainLayout.addWidget(languageLabel, 9, 0)
        mainLayout.addWidget(self.languageCombox, 9, 1)

        mainLayout.addWidget(themeLabel, 10, 0)
        mainLayout.addWidget(self.customColorButton, 10, 1)

        mainLayout.addWidget(templateLabel, 11, 0)

        mainLayout.setSpacing(1)
        mainLayout.setContentsMargins(20, 10, 30, 0)
        mainLayout.setRowStretch(11, 1)

        self.setLayout(mainLayout)

    def initConnect(self):
        self.softwarenameLineEdit.textChanged.connect(self.outputfoldernameLineEdit.setText)
        self.softwarenameLineEdit.textChanged.connect(self.exenameLineEdit.setText)
        self.softwarenameLineEdit.textChanged.connect(self.desktoplinkLineEdit.setText)
        self.customColorButton.clicked.connect(self.customColor)

    def colorqss(self, color):
        style = '''
            QPushButton{
                background-color: %s;
            }
            QPushButton:hover, :pressed
            {
                background-color: %s;
            }
            QPushButton:flat{
                border: none;
            }
            '''%(color, color)
        return style

    def customColor(self):
        colordialog = QtWidgets.QColorDialog(QtGui.QColor("green"))
        colordialog.colorSelected.connect(self.updateColorButton)
        colordialog.exec_()

    def updateColorButton(self, color):
        self.color = "0x" + color.name()[1:]
        self.customColorButton.setStyleSheet(self.colorqss(color.name()))

    def getFormData(self):
        if self.desktoplinkButton.state == 0:
            desktoplink_on = "True"
        else:
            desktoplink_on = "False"
        return {
            "softwarename": self.softwarenameLineEdit.text(),
            "outputfoldername": self.outputfoldernameLineEdit.text(),
            "exename": self.exenameLineEdit.text(),
            "desktoplinkname": self.desktoplinkLineEdit.text(),
            "softwareversion": self.softwareversionLineEdit.text(),
            "softwareauthor": self.softwareauthorLineEdit.text(),
            "softwareemail": self.softwarenameLineEdit.text(),
            "softwarecompany": self.softwarecompanyLineEdit.text(),
            'desktoplink_on': desktoplink_on,
            'language': self.languageCombox.currentText(),
            'background-color': self.color,
            'templateindex':0,
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
        self.initConnect()

    def initData(self):
        pass

    def initUI(self):
        self.setMaximumWidth(200)
        self.countLabel = QtWidgets.QLabel()
        self.countLabel.setObjectName("Count")
        self.countLabel.setFixedSize(100, 100)
        self.countLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.buildButton = BaseToolButton(self.tr("Build"))
        self.buildButton.setFixedWidth(180)
        self.viewButton = BaseToolButton(self.tr("View result"))
        self.viewButton.setFixedWidth(180)

        countLayout = QtWidgets.QHBoxLayout()
        countLayout.addStretch()
        countLayout.addWidget(self.countLabel)
        countLayout.addStretch()

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(countLayout)
        mainLayout.addStretch()
        mainLayout.addWidget(self.buildButton)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(self.viewButton)
        mainLayout.addSpacing(10)
        mainLayout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(mainLayout)

    def initConnect(self):
        self.viewButton.clicked.connect(self.viewResult)
        from dataBase import signal_DB
        signal_DB.count_sin.connect(self.updateCount)

    def viewResult(self):
        toolPath = os.sep.join([os.getcwd(), 'output'])
        if os.path.exists(toolPath):
            QtGui.QDesktopServices.openUrl(QtCore.QUrl("file:///%s" % toolPath))

    def updateCount(self, count):
        self.countLabel.setText(str(count))


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
        # mainLayout.addStretch()
        mainLayout.setContentsMargins(5, 0, 0, 0)
        self.setLayout(mainLayout)

    def initConnect(self):
        self.buildPage.buildButton.clicked.connect(self.build)

    def build(self):
        software = self.setuperPage.getFormData()
        files = []
        for f in self.uploadPage.browerPage.files:
            item = {
                'name': os.path.basename(f),
                'path': f
            }
            files.append(item)
        software['files'] = files
        fd = open(os.sep.join(['tools', 'package', 'package.json']), 'w',encoding='utf8')
        fd.write(json.dumps(software, indent=4))
        fd.close()

        config = generateConfig(software)

        toolPath = os.sep.join([os.getcwd(), 'tools'])

        name = '%s-v%s.exe' % (software['softwarename'], software['softwareversion'])
        if software['templateindex'] > 0:
            template = "InstallerUI%s.exe" % software['templateindex']
        else:
            template = "InstallerUI.exe"
        # print("template is %s" % template)
        if not os.path.exists(os.sep.join([toolPath, template])):
            # print("%s is not exists" % template)
            template = "InstallerUI.exe"

        templatePath = os.sep.join([toolPath, template])

        outputPath = os.sep.join([os.getcwd(), 'output'])
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)

        outputExePath = os.sep.join([outputPath, name])

        flag = generateExe(config, templatePath, outputExePath)

        if flag:
            g = GuiManger.instance()
            res = {
                'dektopClient':"CloudSetuper"
            }
            g.ws.send(json.dumps(res))
