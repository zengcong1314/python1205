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
str = 'adsfdfgfhg'
print(list(str))
def string_reverse2(string):
    new_str = list(str)
    new_str.reverse()
    print(new_str)
    #print(str(new_str))
    return ''.join(new_str)
if __name__ == "__main__":
    print(str)
    print(string_reverse2(str))

#排序
#冒泡排序
#快速排序



