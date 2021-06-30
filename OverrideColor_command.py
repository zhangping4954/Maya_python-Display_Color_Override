#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import Maya_Pyside2_Display_Color_Overrride_UI
reload(Maya_Pyside2_Display_Color_Overrride_UI)


path = 'D:\Maya_python_Display_Color_Override'
if path not in sys.path:
    sys.path.append(path)


import Maya_Pyside2_Display_Color_Overrride_UI
reload(Maya_Pyside2_Display_Color_Overrride_UI)

Maya_Pyside2_Display_Color_Overrride_UI.main()

