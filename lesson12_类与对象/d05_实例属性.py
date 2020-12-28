"""
实例属性：个体（对象）具备的特征，这些特征可以一样，也可以不一样
__init__()方法
不能有返回值
类下面的函数就叫做方法

self ,在类定义过程中，类的里面代表一个实例
"""
class Car:
    #所有的车都具备的属性
    engine = True
    wheel = True
    material = ["塑料","橡胶"]

    def __init__(self,logo,color):
        """初始化方法，初始化函数"""

        print("对象产生时进行的初始化工作")
        print("类里面得self",id(self))
        self.brand = logo #brand是定义的属性，brand属性设置为 logo
        self.col = color  # self 就是实例
        return None
#当__init__有参数时候，
my_car = Car("Tesla","red")
your_car = Car("丰田","white")
print(my_car)
print("类外边的id：",id(my_car))
print(my_car.brand)
#
# #修改实例属性
# my_car.brand = "本田"
# print(my_car.brand)
#
# #类能不能修改实例属性
# #Car.brand="莲花"
# #print(Car.brand) #brand是实例属性，不是整个类都具备得属性，有的车没有牌子，直接获取会报错，获取不到
# Car.brand="莲花"
# print(Car.brand) #定义了类属性
# print(my_car.brand)

