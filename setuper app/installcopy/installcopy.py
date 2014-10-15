#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json

def main():
    folderName  = sys.argv[1]
    pacakgejson = os.sep.join([os.getcwd(), folderName, 'package.json'])
    if os.path.exists(pacakgejson):
        with open(pacakgejson, 'r') as fp:
            config = json.load(fp)

if __name__ == '__main__':
    main()
