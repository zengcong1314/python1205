"""
记录程序运行过程
方便定位问题
"""

class Dog():

    def __init__(self,color):
        print("正在初始化。。。")
        self.color = color
        print("已经定义好了color属性")
        self.ke = "dog"
        print("已经定义好了ke属性")
        try:
            a = []
            a[100]
        except IndexError:
            print("出现了错误！！！！！！！！！！！！！！！")

    def run(self):
        print("狗再跑")

dog = Dog("黑色")