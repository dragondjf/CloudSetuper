#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse

def getOrderFromJson(pacakgejson, args):
    os.chdir(args.package)
    if os.path.exists(pacakgejson):
        with open(pacakgejson, 'r') as fp:
            config = json.load(fp)
        fsize = {}
        for item in config['Files']:
            if isinstance(item, dict):
                filesize = os.path.getsize(item['path'])
                item.update({u"size": filesize})
                fsize.update({filesize: item})
        orderFsize = sorted(fsize.iteritems(), key=lambda d:d[0])
        orderFile = [v for k, v in orderFsize]
        nameOrder = [item['name'] for item in orderFile][::-1]
        sizeOrder = [item['size'] for item in orderFile][::-1]
        pathOrder = [item['path'] for item in orderFile][::-1]
        result = []
        for i in xrange(len(nameOrder)):
            item ={}
            item['name'] = nameOrder[i]
            item['size'] = sizeOrder[i]
            item['path'] = pathOrder[i]
            result.append(item)
    else:
        print "The [%s]  isn't exits!" % pacakgejson
        result = None
    os.chdir('..')
    config['Files'] = result
    return config

def copyFile2Exe(config, args, outPutExe="setup.exe"):
    ftemplate = open(os.path.abspath(args.template), 'rb')
    content = ftemplate.read()
    ftemplate.close()
    os.chdir(args.package)
    for f in config['Files']:
        fp = open(f['path'], 'rb')
        content += fp.read()
        fp.close()
        f.pop('path')
    configBlock = json.dumps(config)
    print configBlock
    content += configBlock
    content += "|%d" % len(configBlock)

    foutput = open(outPutExe, 'wb')
    foutput.write(content)
    foutput.close()
    os.chdir('..')


def main():

    parser = argparse.ArgumentParser(
        prog='installcopy', 
        usage='%(prog)s [options]',
        description='commmand line tool to append files to en [exe] file'
    )

    parser.add_argument('-p', 
        action='store', 
        dest='package',
        default="package",
        help='files in pacakge append to exe')

    parser.add_argument('-t', 
        action='store', 
        dest='template',
        default="InstallerUI.exe",
        help='install ui template exe')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    pacakgejson = os.sep.join([os.getcwd(), args.package, 'package.json'])
    config = getOrderFromJson(pacakgejson, args)

    copyFile2Exe(config, args)


if __name__ == '__main__':
    main()
