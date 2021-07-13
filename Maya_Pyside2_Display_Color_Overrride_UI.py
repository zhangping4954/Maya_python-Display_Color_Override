#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets,QtCore
from PySide2.QtGui import QIcon
import maya.cmds as cm
import maya.OpenMayaUI as Mul
import shiboken2
import maya_path_env
import os
import Maya_PY_Display_Color_Override_ui
import Maya_PY_Display_Color_Override
reload(Maya_PY_Display_Color_Override)
reload(Maya_PY_Display_Color_Override_ui)
reload(maya_path_env)

_win = "Override_Color_Window"


def get_maya_window():
    """
    :return:
    """
    ptr = Mul.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)


class OverrideColor(Maya_PY_Display_Color_Override_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    """
    
    """
    def __init__(self, parent= get_maya_window()):
        """
        :param parent:
        """
        super(OverrideColor, self).__init__(parent)
        self.setupUi(self)
        self.setObjectName(_win)
        self.color_1.setIcon(QIcon(get_icon_path('1')))
        self.color_2.setIcon(QIcon(get_icon_path('2')))
        self.color_3.setIcon(QIcon(get_icon_path('3')))
        self.color_4.setIcon(QIcon(get_icon_path('4')))
        self.color_5.setIcon(QIcon(get_icon_path('5')))
        self.color_6.setIcon(QIcon(get_icon_path('6')))
        self.color_7.setIcon(QIcon(get_icon_path('7')))
        self.color_8.setIcon(QIcon(get_icon_path('8')))
        self.color_9.setIcon(QIcon(get_icon_path('9')))
        self.color_10.setIcon(QIcon(get_icon_path('10')))
        self.color_11.setIcon(QIcon(get_icon_path('11')))
        self.color_12.setIcon(QIcon(get_icon_path('12')))
        self.color_13.setIcon(QIcon(get_icon_path('13')))
        self.color_14.setIcon(QIcon(get_icon_path('14')))
        self.color_15.setIcon(QIcon(get_icon_path('15')))
        self.color_16.setIcon(QIcon(get_icon_path('16')))
        self.color_17.setIcon(QIcon(get_icon_path('17')))
        self.color_18.setIcon(QIcon(get_icon_path('18')))
        self.color_19.setIcon(QIcon(get_icon_path('19')))
        self.color_20.setIcon(QIcon(get_icon_path('20')))
        self.color_21.setIcon(QIcon(get_icon_path('21')))
        self.color_22.setIcon(QIcon(get_icon_path('22')))
        self.color_23.setIcon(QIcon(get_icon_path('23')))
        self.color_24.setIcon(QIcon(get_icon_path('24')))
        self.color_25.setIcon(QIcon(get_icon_path('25')))
        self.color_26.setIcon(QIcon(get_icon_path('26')))
        self.color_27.setIcon(QIcon(get_icon_path('27')))
        self.color_28.setIcon(QIcon(get_icon_path('28')))
        self.color_29.setIcon(QIcon(get_icon_path('29')))
        self.color_30.setIcon(QIcon(get_icon_path('30')))
        self.color_31.setIcon(QIcon(get_icon_path('31')))

    def onClick_Button(self):

        app = QtWidgets.QApplication.instance()

        app.quit()


    @QtCore.Slot(bool)
    def on_color_1_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(1)

    @QtCore.Slot(bool)
    def on_color_2_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(2)

    @QtCore.Slot(bool)
    def on_color_3_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(3)

    @QtCore.Slot(bool)
    def on_color_4_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(4)

    @QtCore.Slot(bool)
    def on_color_5_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(5)

    @QtCore.Slot(bool)
    def on_color_6_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(6)

    @QtCore.Slot(bool)
    def on_color_7_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(7)

    @QtCore.Slot(bool)
    def on_color_8_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(8)

    @QtCore.Slot(bool)
    def on_color_9_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(9)

    @QtCore.Slot(bool)
    def on_color_10_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(10)

    @QtCore.Slot(bool)
    def on_color_11_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(11)

    @QtCore.Slot(bool)
    def on_color_12_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(12)

    @QtCore.Slot(bool)
    def on_color_13_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(13)

    @QtCore.Slot(bool)
    def on_color_14_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(14)

    @QtCore.Slot(bool)
    def on_color_15_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(15)

    @QtCore.Slot(bool)
    def on_color_16_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(16)

    @QtCore.Slot(bool)
    def on_color_17_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(17)

    @QtCore.Slot(bool)
    def on_color_18_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(18)

    @QtCore.Slot(bool)
    def on_color_19_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(19)

    @QtCore.Slot(bool)
    def on_color_20_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(20)

    @QtCore.Slot(bool)
    def on_color_21_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(21)

    @QtCore.Slot(bool)
    def on_color_22_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(22)

    @QtCore.Slot(bool)
    def on_color_23_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(23)

    @QtCore.Slot(bool)
    def on_color_24_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(24)

    @QtCore.Slot(bool)
    def on_color_25_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(25)

    @QtCore.Slot(bool)
    def on_color_26_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(26)

    @QtCore.Slot(bool)
    def on_color_27_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(27)

    @QtCore.Slot(bool)
    def on_color_28_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(28)

    @QtCore.Slot(bool)
    def on_color_29_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(29)

    @QtCore.Slot(bool)
    def on_color_30_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(30)

    @QtCore.Slot(bool)
    def on_color_31_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.override_color_index(31)

    @QtCore.Slot(bool)
    def on_The_default_clicked(self, args=None):
        Maya_PY_Display_Color_Override.DisplayColorOverride.use_defaults()





def get_icon_path(icon_name):
    icon_path = os.path.join(maya_path_env.MAYA_ICON_NAME_PATH, 'color_{0}.png'.format(icon_name))
    if not os.path.isfile(icon_path):
        return icon_path
    return icon_path


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


