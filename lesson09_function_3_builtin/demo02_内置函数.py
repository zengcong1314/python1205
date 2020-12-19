#docs.python.org/zh-cn/3/library/functions.html
#最小值、最大值的内置函数
b = min(1,2,3,6)
print(b)

b = max(1,2,3,6)
print(b)

#学过的内置函数
#print:输出
#input:输入
#type:查看数据类型
#id:生成数据
#len:获取数据的长度（元素总数）
#int\float\bool\str\list\tuple\dict\set:代表对应的数据类型

#最小值、最大值、求和的内置函数
#min\max\sum
#列表、元组
# a = [1,2,3,4]
# b = (1,2,3,4)
# print(sum(a))
# print(sum(a))

#python中高级内置函数
#enumerate:利用它可以同时获得序列类型数据的下标和值

#eval:
#1、取出字符串中的内容，
#2、将字符串str当成有效的表达式来求值并返回计算结果
# print("4+8")
# b = eval("4+8")
# print(b)
#
# a = "{'name':'suifeng'}"
# print(type(a))
# print(type(eval(a)))
# print(eval(a)["name"])

#filter(参数1，参数2)
#参数1：过滤规则的函数
#参数2：要过滤的数据

#zip
title = ["case_id","title","url"]
data = ["登录","http://www.baidu.com"]

totle = zip(title,data)
#print(dict(totle))
print(list(totle))


