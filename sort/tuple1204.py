#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 13:45
# @Author  : zc
# @FileName: tuple1204.py
# @Software: PyCharm
#依次接收用户输入的3个数，排序后打印
#转换int后，判断大小排序，使用分支结构完成
#使用max函数
#使用列表sort方法
#冒泡法

# number1 = int(input("请输入number1："))
# number2 = int(input("请输入number2："))
# number3 = int(input("请输入number3："))
# if number1 > number2:
#     if number1 > number3:
#         if number2 > number3:
#             print(number1,number2,number3)
#         else:
#             print(number1,number3,number2)
#     else:
#         print(number3,number1,number2)
# else:
#     if number3 > number2:
#         print(number3,number2,number1)
#     else:
#         if number3 > number1:
#             print(number2,number3,number1)
#         else:
#             print(number2,number1,number3)

# num1 = int(input("请输入num1："))
# num2 = int(input("请输入num2："))
# num3 = int(input("请输入num3："))
# nums = [num1,num2,num3]
# print(len(nums))
# for i in range (0,len(nums)):
#     for j in range (0,len(nums)-1-i):
#         if nums[j]>nums[j+1]:
#             temp = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = temp
# print(nums)


# num1 = int(input("请输入num1："))
# num2 = int(input("请输入num2："))
# num3 = int(input("请输入num3："))
# nums=[num1,num2,num3]
# sortnum = []
#
# for i in range (0,len(nums)):
#     sortnum.append(max(nums))
#     nums.remove(max(nums))
#     print(nums)
#     print('排序后的字段结果是：{}'.format(sortnum))
# print(sortnum)

num1 = int(input("请输入num1："))
num2 = int(input("请输入num2："))
num3 = int(input("请输入num3："))
nums = [num1,num2,num3]
nums.sort()
print(nums)