#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json

a = {
    "2.png": {
        "path": "../xl2.png"
    }, 
    "3.png": {
        "path": "../xl3.png"
    }, 
    "OutputFolderName": "QFramer", 
    "1.png": {
        "path": "../xl1.png"
    }, 
    "ExeSource.7z": {
        "path": "../ExeSource.7z"
    }, 
    "4.png": {
        "path": "../xl4.png"
    }, 
    "FinishedOpenFlag": True, 
    "InstallerUI.exe": {
        "path": "../InstallerUI.exe"
    }, 
    "HomePage": "http://dragondjf.github.io/", 
    "Icon": {
        "path": "../setup.ico"
    }
}



def main():
    folderName  = sys.argv[1]
    pacakgejson = os.sep.join([os.getcwd(), folderName, 'package.json'])
    if os.path.exists(pacakgejson):
        with open(pacakgejson, 'r') as fp:
            config = json.load(fp)

if __name__ == '__main__':
    main()
