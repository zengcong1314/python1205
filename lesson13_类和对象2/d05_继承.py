"""
一个类继承另一个的类所有属性和方法
包含：Animal 包含狗类
狗类：叫做 Animal类的子类
Animal是父类

继承：他就可以使用父类的所有属性和方法。

当父类和子类具有相同的方法，包括相同的属性，如果自己有，先调用自己

方法重写：子类实现了父类同名的函数，叫做重写
继承的父类里面有重复函数，有继承顺序的，

多重继承:同时继承多个类
"""
class Animal:
    def run(self):
        print("正在跑。。。")

class Dog(Animal):
    def run(self):
        print("狗在跑")
class NotClever:
    def chajia(self):
        print("拆家")

class Erha(Dog,NotClever):
    print("二哈正在跑")

dog = Dog()
dog.run()

erth = Erha()
erth.run()
erth.chajia()
#获取继承的优先调用顺序  所有类的父类object
print(Erha.__mro__)