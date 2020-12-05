# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Time    : 2020/12/3 14:53
# # @Author  : zc
# # @FileName: 1202homework.py
# # @Software: PyCharm
#
#
# 请提交 py 文件，非 py 文件一律打回重做哦。 标注选做的不需要提交：
# 1、现在有字符串：str1 = 'python cainiao 666'
#     1、请找出第 5 个字符。
#     2、请找出第 3 到 第 8 个字符。
str1 = 'python cainiao 666'
print(str1[4])
print(str1[2:8:1])


# 2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！
# （不需要校验数据，都传入数字就可以了。）
price = int(input("请输入橘子价格:"))
weight = int(input("请输入重量:"))
money = price * weight
print(money)

# 3.演练字符串操作
# my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串
# 截取从 开始位置~ 位置6 的字符串
# 从 索引3 开始，每2个字符中取一个字符
# 截取字符串末尾两个字符
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
my_hobby = "Never stop learning!"
print(my_hobby[1:6])
print(my_hobby[:6])
print(my_hobby[3::2])
print(my_hobby[-2:])
#或者
print(my_hobby[18:])
# 4， 总结本节课内容，画出思维导图或者笔记详情。（这节课非常重要，务必进行总结）