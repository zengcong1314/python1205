#使用for打印九九乘法表
for i in range (1,10):
    for j in range (1,i+1):
        print( "{}*{}={}".format(j,i,i*j),end="\t")
    print()

# 你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请依次把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。（不要使用 clear）
black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
for i in range(0,len(black_list)):
    if len(black_list) != 0:
        black_list.pop(-1)
        print(black_list)
print(black_list)

# 编写如下程序
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
weekdays = {"1":"周一","2":"周二","3":"周三","4":"周四","5":"周五","6":"周六","7":"周日"}
list1 = ["1","2","3","4","5"]
list2 = ["6","7"]
while True:
    num  = input("请用户输入0-7范围内数字：")
    if num in list1:
        print(weekdays[num])
    elif num in list2:
        print("周末")
    elif num == "0":
        print("程序退出！")
        break
    else:
        print("输入有误，请重新输入！")

# 使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示用户胜、负还是平局。
info = {1:"石头",2:"剪刀",3:"布",4:"退出"}
import random
print("------石头剪头布游戏开始---------")
print("请按照下面提示出拳：\n石头【1】／剪刀【2】／布【3】/退出【4】")
while True:
    user = int(input("请输入你的选项："))
    computer = random.randint(1,3)
    print("电脑出拳为:",computer)
    if user > 4:
        print("输入错误，请重新输入数字1-4")
    elif user == 1 and computer == 2 :
        print("您的出拳为：{},电脑出拳为:{}，您胜利了".format(info[user],info[computer]))
    elif user == 2 and computer == 3 :
        print("您的出拳为：{},电脑出拳为:{}，您胜利了".format(info[user], info[computer]))
    elif user == 3 and computer == 1:
        print("您的出拳为：{},电脑出拳为:{}，您胜利了".format(info[user], info[computer]))
    elif user == 1 and computer ==1:
        print("您的出拳为：{},电脑出拳为:{}，平局".format(info[user], info[computer]))
    elif user == 2 and computer ==2:
        print("您的出拳为：{},电脑出拳为:{}，平局".format(info[user], info[computer]))
    elif user == 3 and computer ==3:
        print("您的出拳为：{},电脑出拳为:{}，平局".format(info[user], info[computer]))
    elif user == 1 and computer ==3:
        print("您的出拳为：{},电脑出拳为:{}，您输了".format(info[user], info[computer]))
    elif user == 2 and computer ==1:
        print("您的出拳为：{},电脑出拳为:{}，您输了".format(info[user], info[computer]))
    elif user == 3 and computer ==2:
        print("您的出拳为：{},电脑出拳为:{}，您输了".format(info[user], info[computer]))
    else:
        user == 4
        print("游戏结束")
        break

#2，打印 5-999 的所有奇数
for i in range (5,1000):
    if i % 2 != 0:
        print(i,end=" ")



# 使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a = [1,7,4,89,34,2]
for i in range (0,len(a)-1): # 这个循环负责设置冒泡排序进行的次数
    for j in range (0,len(a)-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            print(a)
print(a)


