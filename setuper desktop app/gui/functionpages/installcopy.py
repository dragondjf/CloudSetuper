#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import argparse

def getOrderFromJson(pacakgejson, args):
    pwd = os.getcwd()
    os.chdir(args.package)
    if os.path.exists(pacakgejson):
        with open(pacakgejson, 'r') as fp:
            config = json.load(fp)
        fsize = {}
        for item in config['files']:
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
        print("The [%s]  isn't exits!" % pacakgejson)
        result = None
    os.chdir(pwd)
    config['files'] = result[::-1]
    config['ppt_order'] = [item['name'] for item in config['files']]
    config['ppt_order']= config['ppt_order'][0: -1]
    print(config)
    return config


def generateConfig(config):
    fsize = {}
    for item in config['files']:
        if isinstance(item, dict):
            filesize = os.path.getsize(item['path'])
            item.update({u"size": filesize})
            fsize.update({filesize: item})
    orderFsize = sorted(fsize.items(), key=lambda d:d[0])
    orderFile = [v for k, v in orderFsize]
    nameOrder = [item['name'] for item in orderFile][::-1]
    sizeOrder = [item['size'] for item in orderFile][::-1]
    pathOrder = [item['path'] for item in orderFile][::-1]
    result = []
    for i in range(len(nameOrder)):
        item ={}
        item['name'] = nameOrder[i]
        item['size'] = sizeOrder[i]
        item['path'] = pathOrder[i]
        result.append(item)

    config['files'] = result[::-1]
    config['ppt_order'] = [item['name'] for item in config['files']]
    config['ppt_order']= config['ppt_order'][0: -1]

    return config


def generateExe(config, templatePath, outputPath):
    ftemplate = open(templatePath, 'rb')
    content = ftemplate.read()
    ftemplate.close()
    for f in config['files']:
        fp = open(f['path'], 'rb')
        content += fp.read()
        fp.close()
        f.pop('path')
    configBlock = json.dumps(config)
    content += configBlock.encode("utf8")
    content += str("|%d" % len(configBlock)).encode("utf8")

    foutput = open(outputPath, 'wb')
    foutput.write(content)
    foutput.close()


def copyFile2Exe(config, args):
    ftemplate = open(os.path.abspath(args.template), 'rb')
    content = ftemplate.read()
    ftemplate.close()
    pwd = os.getcwd()
    os.chdir(os.path.abspath(args.package))
    for f in config['files']:
        fp = open(f['path'], 'rb')
        content += fp.read()
        fp.close()
        f.pop('path')
    configBlock = json.dumps(config)
    content += configBlock
    content += "|%d" % len(configBlock)
    buildtime = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(int(time.time()))).decode('UTF8')

    foutput = open(args.output, 'wb')
    foutput.write(content)
    foutput.close()
    os.chdir(pwd)


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

    parser.add_argument('-u', 
        action='store', 
        dest='output',
        default="setup.exe",
        help='output exe name')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    if os.path.exists(os.path.abspath(args.package)):
        pacakgejson = os.sep.join([os.path.abspath(args.package), 'package.json'])
        config = getOrderFromJson(pacakgejson, args)
        copyFile2Exe(config, args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
