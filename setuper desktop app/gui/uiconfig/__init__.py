#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json


__softwarename__ = 'CloudSetuper'
__author__ = ""
__url__ = ""
__description__ = '''
    This is a SoftwareFrame based on PyQt5.
'''
__logoico__ = os.sep.join(['gui', 'skin','images','CloudSetuper.ico'])
__version__ = '1.0.0'


mainwindow = {
    'title': __softwarename__,
    'size': (0.6, 0.8),
    'minsize': (0.4, 0.3),
    'icon': __logoico__,
    'fullscreenflag': False,
}

logo_ico = __logoico__
logo_img_url = os.sep.join(['gui', 'skin','images','logo.png'])
logo_title = u''

from .dialogconfig import dialogsettings
from .frameqss import frameqss, makeFrameQss

try:
    with open(os.sep.join([os.getcwd(), 'options', 'windowsoptions.json']), 'r') as f:
        windowsoptions = json.load(f)
except:
    windowsoptions = {
        'mainwindow': mainwindow,
        'splashimg': os.sep.join([os.getcwd(), 'gui', 'skin', 'images', 'splash.png']),
        'splashflag': False,
        'frameqss': frameqss
    }
    windowsoptions.update(dialogsettings)
