"""
异常：程序发生了意想不到的错误，报错
程序遇到异常通常会终止运行
"""

# ImportError:无法引入模块或包
# IndexError：下标索引超出序列边界
# a = '1234'
# print(a[100])
# NameError：使用一个还未赋予对象的变量
# print(a)
# SyntaxError：代码逻辑语法出错，不能执行；不能去捕获
# print(a))
# TypeError：传入的对象类型与要求不符
# print("a" + 1)
# ValueError：传入一个不被期望的值，即使类型正确
# print(int("a"))
# KeyError：试图访问你字典里不存在的键
# d = {"a":1,"b":2}
# print(d["c"])
# IOError：输入输出异常，文件操作
# ZeroDivisionError
# print(3/0)

print("无论如何都运行")

# 定位异常
# 1、找到异常类型
# 2、异常分析
# 3、找到触发异常的代码