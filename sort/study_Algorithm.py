#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 22:59
# @Author  : zc
# @FileName: 01.py
# @Software: PyCharm
#写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

#斐波那契数列

#冒烟
#大整数加法
# n = int(input())
#
# for x in range (0,n):
#     a = input()
#     n,m = a.split(' ')
#     print(int(n)+int(m))


# 1.按升序合并如下两个list, 并去除重复的元素
#去重的方法有多种
#1、集合去重 list(set(list3))
# list1 = [2, 3, 8, 4, 9, 5, 6]
#
# list2 = [5, 6, 10, 17, 11, 2]
# list3 = list1+list2
# print(list3)
# list3.sort()
# print(list3)
# print(list(set(list3)))
#2、可以通过遍历去重，复制一个列表，清除原列表，遍历复制列表中的元素，如果不存在原列表，就新增
# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
# list3 = list1+list2
# temp_list=list3[::-1]
# list3.clear()
# for i in temp_list:
#     if i not in list3:
#         list3.append(i)
# print(list3)

#写一个函数, 输入一个字符串, 返回倒序排列的结果
# str = 'adsfdfgfhg'
# def string_reverse(string):
#     return string[::-1]
#
# if __name__ =="__main__":
#     print(str)
#     print(string_reverse(str))

#把字符串变成列表，用列表的reverse函数
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# str = 'adsfdfgfhg'
# print(list(str))
# def string_reverse2(string):
#     new_str = list(str)
#     new_str.reverse()
#     print(new_str)
#     #print(str(new_str))
#     return ''.join(new_str)
# if __name__ == "__main__":
#     print(str)
#     print(string_reverse2(str))

#排序
#冒泡排序
#快速排序

#json与字典中相互转化
# import json
# data_dict = "{'name':'zc','age':18}"
# print(type(data_dict))
# data_json = '{"name":"zc","age":18}'
# print(type(data_json))
# json.loads(data_json)
# print(type(data_json))

#完美数 一般指完全数，它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的真因子之和，则称该数为“完全数”
# a = []
# for i in range(1,1000):
#     s = 0
#     for j in range(1,i):
#         if i%j == 0 and j < i:
#             s = s+j
#     if s == i:
#         print(i)
#         a.append(i)
# print("1000以内的完全数为：",a)

#统计一个文本中a(A)出现的次数

#统计一个文本中(TXT)文件里出现最多的IP地址，并打印出来

#二叉树 中序遍历
#判断一个字符串是不是回文串？ 正读与反读都一样的字符串
# str = input("请输入一个字符串：")
# sort_str=str[::-1]
# if str == sort_str:
#     print("这个字符串{}是回文字符串".format(str))
# else:
#     print("这个字符串{}不是回文字符串".format(str))
#tcp三次握手，四次挥手
#输入一个网址之后的流程
#http是哪层的协议
#python中is和==的区别 is id值要一致，==id值不用一致
#设计一下抖音上下滑动视频的测试用例
#栈和堆的区别

#输入一个字符串空格切割在统计每个字母出现的次数
#str = input("请输入一个字符串：")
str = "sdsfsdf"
str = ' '.join(str)
print(str)
list1 = str.split(' ')
print(list1)
for i in set(str):
    if list1.count(i) >= 1:
        print("字符串{}出现的次数为{}：".format(i, list1.count(i)))


