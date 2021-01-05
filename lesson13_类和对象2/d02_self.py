"""
self ,代表在类定义过程中，表示一个对象。self占坑
可以改成任意的变量

self 在类定义里面表示对象本身，可以修改成其他的变量，但是不要改规范

实例属性的定义 self.属性
变量不等于属性
类变量，实例变量 就是类属性，实例属性
"""

class Car:
    #所有的车都具备的属性
    engine = True
    wheel = True
    material = ["塑料","橡胶"]

    def __init__(self,logo ,color): #logo color是变量，跟属性没关系
        """初始化方法，初始化函数"""
        print("对象产生时进行的初始化工作")
        print("类里面得",id(self))
        self.brand = logo #brand是定义的属性，self.brand给属性赋值，设置为 logo
        self.col = color  # self 就是实例
my_car = Car("丰田","紫色")
print("类外面",id(my_car))
