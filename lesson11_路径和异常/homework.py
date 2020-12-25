# 第一题
# 使用函数完成以下程序：体育课根据身高分组，你输入身高（cm），程序显示你分入篮球队还是足球队：
# 如果大于等于 170， 显示“你适合打篮球”；
# 身高小于 170，显示“你适合踢足球”；
# 输入异常，提示“数据错误”
# 示例：
# 请输入你的身高：180.2
# 你是篮球巨星
def grouping():
        try:
            height = float(input("请输入你的身高："))
            if height >= 170:
                print("你适合打篮球")
            elif height < 170:
                print("你适合踢足球")
        except ValueError as e:
            #print(e)
            print("数据错误")
grouping()


# 第二题
# 查找当前文件目录下是否存在 tests 子目录，如果存在，打印出 tests 目录路径；如果不存在，创建这个子目录。
import os
def find_file(filename):
    if os.path.isdir(filename):
        print("当前的文件路径为:",os.path.dirname(__file__))
    else:
        os.mkdir(filename)
find_file("tests")

# 第三题
# 使用 x 模式在当前目录下的 demo.txt 文件中写入 “类和对象没有想象的那么难”， 如果该文件已经存在，打印“文件已经存在”
import os
def write_file(filename):
    # 如果文件存在，则提示
    if os.path.exists(os.path.join(os.path.dirname(__file__),filename)):
        print(os.path.dirname(__file__))
        print(os.path.join(os.path.dirname(__file__),filename))
        print("文件已经存在")
    else:
    # 如果文件不存在，则创建写入
        with open(filename,mode='x',encoding="UTF-8") as f:
            f.write("类和对象没有想象的那么难")
write_file("demo.txt")

# 第四题：编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
price = input("请输入橘子价格：(单位：元／斤)")
weight = input("请输入用户购买橘子的重量:(单位：斤)")
try:
    pay_money = round(float(price) * float(weight),2)
    print(pay_money)
except Exception as e:
    print("数据无效")