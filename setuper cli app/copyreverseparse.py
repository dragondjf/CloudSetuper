#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json

def getfiles(path):
    '''
        获取指定path下的所有文件列表
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.sep.join([dirpath, filename]))
    return files

for f in getfiles("package/"):
    if f.endswith(".exe"):
        fp = open(f, 'rb')
        content = fp.read()
        fp.close()
        last_char_100 = content[-100:] # 取最后100个字符

        index_I = last_char_100.rindex("|") # 从最后100字符末端取 '|' 字符的位置

        configCount = last_char_100[last_char_100.rindex("|") + 1:]  # 取cofig长度
        configEndIndex = len(configCount) + 1 # 取config尾偏移量

        configContent = content[-(int(configCount) + configEndIndex): -configEndIndex] #取config内容
        config = json.loads(configContent) # 将字符串config 转化成 字典对象
        print f
        print config["Files"]

# 其他资源文件按照同样的方式按照Files里面的顺序依次解析
