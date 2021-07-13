#!python3
import subprocess
import os
import maya_path_env

MAYA_PATH = maya_path_env.MAYA_ICON_PATH
_env = os.environ.copy()
_env['MAYA_ENV'] = MAYA_PATH
subprocess.Popen('D:/Program Files/Maya2018/bin/maya.exe', env=_env)

