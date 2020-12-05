#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 13:53
# @Author  : zc
# @FileName: demo01.py
# @Software: PyCharm
"""
pip：安装python插件、python库、python包
-requests
-openyxl

注释不是给机器看的，不是代码，给人看，说明代码的作用
   -单行注释，#
   -多行注释 '''注释'''
缩进
   python 是根据缩进来组织代码块的。:
   从现在开始，所有的python代码顶格写
变量：
    1*2*3*4*5
    变量：存储数据，变
    常量：不变的数据
变量命名：
      - 字母，数字和下划线_，其他的都不可以@，中文
      - 不能以数字开头
      - 不能是python内置的关键字；贵族号码，return，def,if
      - 变量最重要的是能“见名知义”
      拼音不要用
      缩写尽量不要用
注释快捷键：ctrl + /

"""

#把什么内容打印到屏幕上
print("python36期全部都是大佬")

#注释
print("注释")

#先存储1，变量赋值
a = 1
a = a * 2
print(a)
a = a * 3
a = a * 4
a = a * 5
print(a)

import keyword
print(keyword.kwlist)

#变量练习题：
name = "yuz"
name_other = "wang"
full_name = name + name_other
print(full_name)

name = "wen"
print(name)
#前面的值会被覆盖掉

none = 1
print(none)



