# 1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.remove("矮穷丑")
print(info)
# info.pop(3)
# print(info)
# del info[3]
# print(info)
#
# 2、现在有一个列表 li2=[1，2，3，4，5]，
# 请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
li2=[1,2,3,4,5]
li2.insert(0,0)
li2.insert(4,66)
li2.extend([11,22,33])
print(li2)

#请写出删除列表中元素的方法，并说明每个方法的作用
li2.remove(3)#删除值为3的一个元素
print(li2)
li2.pop(5) # 删除索引值为5的元素
print(li2)
del li2[0] # 删除索引为0的元素
print(li2)
li2.clear()# 清空列表当中的元素
print(li2)

# 一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
# 1、 (11)
print(type((11))) #整形int（11）为不可变类型
# 2、 [11，22]
print(type([11,22])) #列表为可变类型
# 3、 ([11,22,33])
print(type(([11,22,33]))) #列表为可变类型

# 二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
# 删除 77，88，99这三个元素
li = [11,22,33,22,22,44,55,77,88,99,11]
li.remove(77)
li.pop(7)
del li[7]
print(li)

# 三，将上个作业的相亲节目用列表实现
# 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄，
info = []
info.extend(["曾聪","femal",18])
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
info.extend([160,13967898761])
print("增加身高和联系方式后信息为：{}".format(info))
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
info.pop(4)
print("删除联系方式后的信息为：{}".format(info))
#
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
info[0] = "兮洛"
info.append("兮洛")
info[3] = 165
print("修改后的花名为：{}，身高为{}".format(info[0],info[3]))
# e, 你进一步添加自己的兴趣，至少需要 3 项。
# info.extend(["看书","芭蕾","瑜伽"])
info.append(["看书","芭蕾","瑜伽"])
info.extend(["看书","芭蕾","瑜伽"])
print(info)