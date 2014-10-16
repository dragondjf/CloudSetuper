#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json


f = open("package/setup.exe", 'rb')
content = f.read()
f.close()
last_char_100 = content[-100:] # 取最后100个字符

index_I = last_char_100.rindex("|") # 从最后100字符末端取 '|' 字符的位置

configCount = last_char_100[last_char_100.rindex("|") + 1:]  # 取cofig长度
configEndIndex = len(configCount) + 1 # 取config尾偏移量

configContent = content[-(int(configCount) + configEndIndex): -configEndIndex] #取config内容
config = json.loads(configContent) # 将字符串config 转化成 字典对象
print config["Files"]

# 其他资源文件按照同样的方式按照Files里面的顺序依次解析
