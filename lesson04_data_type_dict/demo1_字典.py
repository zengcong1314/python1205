#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 14:43
# @Author  : zc
# @FileName: demo1_字典.py
# @Software: PyCharm
a = "hello"
a = "word"
print(a)
#列表尽量存储的是意义相近的元素
#贴标签
#字典
#字典的表示{}
#空的字典{}
movies = {}
print(type(movies))
print(len(movies))

#字典公式：{key:value,key1:value1,key2:value2}
movies = {"favor":"画皮",
          "first_movies":"蜡笔小新",
          "second_movies":"上海堡垒",
          "hate":"心花怒放",
          "cried":"你的名字"
          }
#通过 key 获取某个值
print(movies["favor"])
print(movies["hate"])
#字典不能切片 没有同时获取多个值的操作 ，字典存在计算机中内存中不是存在一起的

#key 是有要求的
#第一种情况：如果一个字典当中有2个key是一样的会怎么办？
#字典里面可以存在重复的key吗？？
#作为一个合法的字典，key不应该有重复的，是无序的
movies = {"favor":"画皮",
          "first_movies":"蜡笔小新",
          "second_movies":"上海堡垒",
          "hate":"你的名字",
          (1,2,3):"大话西游",
          {1:3}:"大话西游23"
          }
#key使用list报错：TypeError: unhashable type: 'list'
#list可以作为key吗？不可以
#元组可以吗？可以
#字典可以吗？
#key:字典不可以，可变类型（列表,字典）不能作为key
#key:不可变类型（元组、字符串、整数）可以作为key
print(movies[(1,2,3)])

