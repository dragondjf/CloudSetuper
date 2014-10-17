import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [""]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "installcopy",
        version = "1.0",
        description = "Command Line for copy fiel to exe!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("installcopy.py", base=base)])
