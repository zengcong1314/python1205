"""
类属性，所有成员都具备的特征
表示：在类定义的下面去定义变量
类属性 == 类变量

获取类属性 Car.wheel
"""
class Car:
    #所有的车都具备的属性
    engine = True
    wheel = True
    material = ["塑料","橡胶"]
    #颜色、大小、牌子

# 类属性
print(Car.wheel)
print(Car.material)

# 类属性的修改
Car.wheel = False
print(Car.wheel)

# 对象能不能获取类属性？？ 可以
my_car = Car()
print(my_car.material)

# 对象修改对应的属性
# 对象修改属性不影响整个类
my_car.material = ["塑料"]
print(my_car.material)
print(Car.material)
