"""
每个函数都有返回值，在return后面
如果没有写，默认return None

函数的返回值，可以通过一个变量去接收

函数为什么要有返回值？
"""
def print_all_dalao():
    """打印所有的大佬 Docstring 文档字符串，说明函数的作用"""
    #函数体：运行函数的时候会执行的代码
    print("1级大佬旧梦")
    print("2级大佬阿吉")
    print("3级大佬NiKi")
#调用的时候不需要缩进
res = print_all_dalao()
print("return value:",res)

a = 2
def add():
    b = a + 3
    return b
print(add())

def add(a,b):
    c = a + b - 1
    #return c
    print("函数内部",c)

print("函数的返回值",add(3,4))