#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 22:59
# @Author  : zc
# @FileName: 01.py
# @Software: PyCharm
#写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

a="abcd"
b=a[::-1]
print(b)

seq = [3,1]
seq.append(seq[0]+seq[1])
print(seq)



# a = "hello"
# b = "hello"
# print(id(a))   # 输出 140506224367496
# print(id(b))   # 输出 140506224367496
# print(a is b)  # 输出 True
# print(a == b)  # 输出 True



a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))   # 输出 140506224299464
print(id(b))   # 输出 140506224309576
print(a is b)  # 输出 False
print(a == b)  # 输出 True