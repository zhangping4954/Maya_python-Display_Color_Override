#!/usr/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.OpenMaya as om


class DisplayColorOverride(object):

    """
    1:创建获取选择模型Shapes节点的方法
    """

    @classmethod
    def shape_nodes(cls):
        """
        创建获取节点的shape_nodes()函数 利用ls 命令获取节点名称 赋值给selection 变量
        """
        selection = cmds.ls(selection=True)
        if not selection:
            """
            if判断如果selection 是空的则返回 None 反之则继续执行下列代码
            """
            return None

        # 创建空的shapes 列表
        shapes = []
        for node in selection:
            """
            循环selection（选择的模型名称）用listRelatives命令获取shapes 名称
            在以extend 方法 逐个将获取好的名称加入到shapes 空列表中
            """
            shapes.extend(cmds.listRelatives(node, shapes=True))
        # 最后返回 shapes 列表
        return shapes


# 定义一个常量32 用来判断颜色数值范围是否超过或等于32 因为颜色数值范围只有0-31
    MAX_OVERRIDE_COLORS = 32

    @classmethod
    def override_color_index(cls, color_index):
        """
        创建辨别颜色信息数值范围函数
        """

        if color_index >= cls.MAX_OVERRIDE_COLORS or color_index < 0:
            """
            判断输入的color_index数值>= 大于等于MAX_OVERRIDE_COLORS（32）或者 color_index数值< 0 小于零
            则提示一个错误 并返回 False
            """
            om.MGlobal.displayError(" 输入的数值超出范围,（请输入0-31）")
            return False

        # 获取先择正确的shape_nodes列表 赋值给shapes 变量
        shapes = cls.shape_nodes()
        if not shapes:
            """
            判断shapes是否为空的 如果为空 则返回一个错误提示用户 选择模型
            """
            om.MGlobal.displayError(" Select the model")
            return False

        for shape in shapes:
            """
            循环选择好的模型 分别执行overrideEnabled打开覆盖命令以及overrideColor颜色设定覆盖命令
            """
            cmds.setAttr("{0}.overrideEnabled".format(shape), 1)
            cmds.setAttr("{0}.overrideColor".format(shape), color_index)
        return True

    @classmethod
    def use_defaults(cls):
        """
        关闭所有选择好的模型为默认颜色线框覆盖函数（蓝色线框）
        """
        # 获取先择正确的shape_nodes列表 赋值给shapes 变量
        shapes = cls.shape_nodes()
        if not shapes:
            """
            判断shapes是否为空的 如果为空 则返回一个错误提示用户 选择模型
            """
            om.MGlobal.displayError("Select the model")
            return False

        for shape in shapes:
            cmds.setAttr("{0}.overrideEnabled".format(shape), 0)
        return True















