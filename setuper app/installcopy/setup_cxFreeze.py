# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup, Executable

sys.argv.append('build')

def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


def getfiles(path):
    '''
        获取指定path下的所有文件列表
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.sep.join([dirpath, filename]))
    return files

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [""]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "installcopy",
        version = "1.0",
        description = "Command Line for copy fiel to exe!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("installcopy.py", base=base, targetDir="distwin")])


for item in ['build']:
    delete_file_folder(item)
