"""
*b表示不定长参数：长度不固定，剩下的我全要
接收所有剩下的位置参数
多个数据，要放到一个变量，元组。
一个*号拆列表、元组的包
两个*号拆字典的包

"""

# def add(a,*b,c=9):
#     print("a:",a)
#     print("b",b)
#     print("c", c)
# add(4,5,6,7,c=9)

# *b 只能接收位置参数
# def add(a,*b):
#     print("a:",a)
#     print("b",b)
# add(4,5,6,7,c=9)

# **kw,接收关键字参数，kw得到的是字典
#不定长参数是函数定义的时候去接收多个值
# def add(a,*b,**kw):
#     print("a:",a)
#     print("b:", b)
#     print("kw", kw)
# add(4,5,6,7,c=9,d="hello")

def add(a,*b,**kw):
    print("a:",a)
    print("b:", b)
name = "yuz"
dalao = ["zaizai","aschool"]
# add(name,dalao)
# #变量前面加*号时，符号去掉，拆掉左右两边表示方法，做成2个参数放进来，叫做拆包（主要指列表和元组）
# add(name,*dalao)
# add("yuz","zaizai","achool")
#
#
# adict = {"you":"hello"}
# add(name,*dalao,**adict)
# add("yuz","zaizai","achool",you="hello")

#
def minus(a,**kw):
    print(a)
    print(kw)
name = "yuz"
# a = name
info = {"age":18,"gender":"男"}
minus(name,age=18,gender="男")
#minus(name,info)#info是位置参数
minus(name,**info)

# 形式参数，实际参数
# 位置参数 一一对应，顺序和数量都要对上
# 关键字参数和默认参数
# 不定长参数。 *args  **Kwargs