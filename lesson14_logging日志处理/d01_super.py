"""super函数
子类的方法，想调用父类的方法,超继承

"""
class Animal:

    def __init__(self,ke,color):
        self.ake = ke
        self.acolor = color


    def run(self):
        print("正在跑。。。")

    def eating(self):
        print("正在吃食物。。。")


class Dog(Animal):
    def __init__(self,dog_color,kind):
        # 调用父类的初始化函数，然后再定义自己的特征
        # self.zcolor = color
        super().__init__("dog",dog_color)
        self.akind = kind

    def run(self):
        # 想调用父类的方法
        # a = Animal()
        # a.run()
        # 如果遇到多重继承，优先使用第一顺位，第一顺位找不到，使用第二顺位
        # super().run()
        print("狗在跑")
        super().eating()

# my_dog = Dog()
# my_dog.run()

#初始化 animal
animal = Animal("dog","black")

#初始化 dog
dog = Dog("black","sd")
print(dog)
print(dog.ake)
print(dog.akind)
