"""
放在类里面的函数就叫方法。（method）
特征是属性，行为是方法
方法：代表类或者实例的行为

方法的调用：函数前面加类与对象调用
__init__  类()自动调用这个方法
实例方法：就是一个对象（个体）特有的行为。实例属性
类方法：整个类具有的行为
普通方法：在类下面，普通方法就是实例方法。调用，普通实例方法：obj.方法（）
带有self的是实例方法

类方法:类方法会在方法上面加一个声明，@classmethod
类方法和实例方法区别：
1、类方法会在方法上面加一个声明，@classmethod
2、实例方法只能通过实例调用
3、类方法可以通过实例与类调用

静态方法（static method）：在方法中，不需要用到对象(self)，又不需要用到类（cls）
当你需要把一个普通的函数放在类下面的时候，就可以使用静态方法，方便管理

用的最多的是实例方法，实例方法一定有self
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

    def drive(self,distance):
        """开车"""
        print("{}开起来非常快,而且可以续航{}公里".format(self,distance))

    @classmethod
    def fly(cls): #现在的self不是对象，表示是整个类 self一般表示的是对象，实例，所以改为cls
        """飞"""
        print("{}正在飞".format(cls))

    @classmethod
    def other_class_method(cls):
        print("other")

    @staticmethod
    def baoyang():
        """和类，和对象没有关系
        它就不应该被定义成实例方法"""
        print("正在保养。。。")



your_car = Car("h","黑色")
# your_car.drive(800)
#
# #实例调用，实例可以调用类方法（类方法，所有的实例都有此行为，所以实例可以调用） ，实例方法只能通过实例调用
# your_car.fly()
# #类调用类方法 ，类方法可以通过类调用
# Car.fly()
#
# #静态方法怎么调用？ 类或对象都可调用
# Car.baoyang()
# your_car.baoyang()

