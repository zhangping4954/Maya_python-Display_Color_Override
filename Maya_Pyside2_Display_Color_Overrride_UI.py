#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
import maya.cmds as cm
import maya.OpenMayaUI as Mul
import shiboken2
import Maya_PY_Display_Color_Override_ui
reload(Maya_PY_Display_Color_Override_ui)

_win = "Override_Color_Window"


def get_maya_window():
    """
    :return:
    """
    ptr = Mul.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)


class OverrideColor(Maya_PY_Display_Color_Override_ui.Ui_MainWindow,QtWidgets.QMainWindow):
    """
    
    """
    def __init__(self, parent= get_maya_window()):
        """
        :param parent:
        """
        super(OverrideColor,self).__init__(parent)
        self.setupUi(self)
        self.setObjectName(_win)


def main():
    """
    :rtype: object
    """
    if cm.window(_win, exists=True):
        cm.deleteUI(_win)
    win = OverrideColor()
    win.show()


if __name__ == '__main__':
    main()

