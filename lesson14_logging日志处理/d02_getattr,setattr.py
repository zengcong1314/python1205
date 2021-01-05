"""
super函数
子类的方法想调用父类的方法，超继承
"""


class Dog():
    def __init__(self,color):
        self.color = color
        self.ke = "dog"

    def run(self):
        print("狗在跑")


# getattr 获取某个属性 内置函数
# setattr 设置某个属性
my_dog = Dog("black")
# 获取属性
print(my_dog.color)

# 用户自己控制获取哪个属性
prop = input("请输入你想获取的狗的属性：")
#print(my_dog)
value = getattr(my_dog, "ke")
print(value)

value = getattr(my_dog,prop)
print(value)

# 获取属性 color
dog = Dog("黑色")
print(dog.color)

#方法二
print(getattr(dog,"color"))
#方法三
prop = "color"
print(getattr(dog,prop))

#不存在的属性，如果找不到该属性，就得到默认值 男
# 如果不传默认值，会报错
print(getattr(dog,"gender","男"))

# setattr
setattr(dog,"gender","女")
print(dog.gender)

ret = getattr(dog,"color","red")
print(ret)

ret = getattr(dog,"boyfriend","hero")
print(ret)
# 没有boyfriend 不会创建这个属性，hero只是个默认值
# hero 只是普通的字符串，赋值给ret
print(dog.boyfriend)