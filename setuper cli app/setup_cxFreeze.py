# -*- coding: utf-8 -*-
import sys
import os
import shutil
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

def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    if not os.path.isdir(dst):
        os.makedirs(dst)
        
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                if os.path.isdir(dstname):
                    os.rmdir(dstname)
                elif os.path.isfile(dstname):
                    os.remove(dstname)
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors)


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [""]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None


if __name__ == '__main__':

    for item in ['build', 'dist', 'distwin']:
        delete_file_folder(item)

    setup(  name = "installcopy",
            version = "1.0",
            description = "Command Line for copy fiel to exe!",
            options = {"build_exe": build_exe_options},
            executables = [Executable("installcopy.py", base=base)])

    shutil.copytree(os.sep.join([os.getcwd(), 'build', "exe.win32-2.7"]), os.sep.join([os.getcwd(), "distwin"]))
    shutil.copytree(os.sep.join([os.getcwd(), 'package']), os.sep.join([os.getcwd(), "distwin", "package"]))

    for item in ['InstallerUI.exe', 'InstallerUI1.exe']:
        shutil.copyfile(os.sep.join([os.getcwd(), item]), os.sep.join([os.getcwd(), "distwin", item]))

    for item in ['build']:
        delete_file_folder(item)

