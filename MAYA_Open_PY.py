#!python3
import subprocess
import os

MAYA_PATH = os.path.dirname(os.path.realpath('MAYA_Open_PY.py'))
_env = os.environ.copy()
_env['MAYA_ENV'] = MAYA_PATH
subprocess.Popen('D:/Program Files/Maya2018/bin/maya.exe', env=_env)

