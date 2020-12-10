# 1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），
# 如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
from decimal import Decimal
price = int(input("请输入购买价格："))
if  0 < price <50:
    print("折扣为{}，最终购买价格为：{}".format(0,price))
elif 50 <= price <= 100:
    print("折扣为{}，最终购买价格为：{}".format(0.1,Decimal(str(price))*Decimal(str(1-0.1))))
else:
    print("折扣为{}，最终购买价格为：{}".format(0.2,Decimal(str(price))*Decimal(str(1-0.2))))


# 2 判断是否为闰年
# 提示:
# 输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
# 什么是闰年，请自行了解（需求文档没有解释）
year = int(input("请输入有效的年份："))
if year % 4 == 0 and year % 100 != 0:
    print("{}是普通闰年".format(year))
elif year % 400 == 0:
    print("{}是世纪闰年".format(year))
else:
    print("{}不是闰年".format(year))


# 3.求三个整数中的最大值
# 提示：定义 3 个变量
#方法一：
num1 = int(input("请输入整数值："))
num2 = int(input("请输入整数值："))
num3 = int(input("请输入整数值："))
max_num = max(num1,num2,num3)
print("最大值为：{}".format(max_num))

#方法二：
num1 = int(input("请输入整数值："))
num2 = int(input("请输入整数值："))
num3 = int(input("请输入整数值："))
if num1 > num2:
    if num3 > num1:
        print("最大值为：",num3)
    else:
        print("最大值为：", num1)
else:
    if num2 < num3:
        print("最大值为：", num3)
    elif num3 < num2:
        print("最大值为：", num2)

# 4， 总结数据运算，做成笔记或者思维导图