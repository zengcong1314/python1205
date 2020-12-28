
def eating(name,sex,age):
    print('{}正在吃狗粮，它的性别是{}，年龄是{}'.format(name,sex,age))

def bark(name,sex,age):
    print('{}正在叫，显然是饿了，它的性别是{}，年龄是{}'.format(name,sex,age))

def bath(name,sex,age):
    print('{}正在洗澡，它的性别是{}，年龄是{}'.format(name,sex,age))

# name = 'single dog'
# sex = '男'
# age = 3
# eating(name,sex,age)
# bark(name,sex,age)
# bath(name,sex,age)




class Dog:
    def __init__(self, name, sex, age):
        self.name = name
        self.gender = sex
        self.age = age

    def eating(self):
        print('{}正在吃狗粮，它的性别是{}，年龄是{}'.format(
            self.name,
            self.gender,
            self.age))

    def bark(self):
        print('{}正在叫，显然是饿了，它的性别是{}，年龄是{}'.format(
            self.name,
            self.gender,
            self.age))


    def bath(self):
        print('{}正在洗澡，它的性别是{}，年龄是{}'.format(
            self.name,
            self.gender,
            self.age))

name = 'single dog'
sex = '男'
age = 3
single_dog = Dog(name,sex,age)
single_dog.eating()
single_dog.bark()
single_dog.bath()

#类与对象可以帮我们存储各个不同的函数需要用到的共同的变量
