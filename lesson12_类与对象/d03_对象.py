"""
对象（object）是一类事务中的一个成员（个体），object的中文是东西，对象又被称为实例
对象（object），实例
内存地址相同，表示的是同一个对象，数据
可以通过id(object)获取
"""
#第一种
class Car:
    pass

my_car = Car() #实例化
# 先有类才有对象
your_car = Car()
suifeng_car = Car()

#<__main__.Car object at 0x000001D35FB4F160> Car的对象在内存中的位置，同一个数值是同一个对象
print(my_car)
print(id(my_car))
print(your_car)
print(suifeng_car)


print(Car() == Car()) #False 对象与对象进行比较

# 类和对象
print(Car)
print(Car())

print(Car == Car) #类与类比较  True

