#变量，局部变量和全局变量
#局部：在函数体或者代码块里面定义的变量
#全局：文件里面顶格定义的变量

#局部作用域能不能获取全局变量 YES
#全局作用域能不能获取局部变量  NO

#局部作用域能不能修改全局变量 No global
#全局作用域能不能修改局部变量 No

# def add(a,b):
#     c = a + b
#     return c + 2
#
# a = 2
# b = 3
# print(add(a,b))

#局部作用域能不能获取全局变量 可以
# a = "随风"
# def add():
#     b = a + "王"
#     print(b)
#     return None
# add()

#全局作用域能不能获取局部变量
#不能直接获取局部变量，通过return返回后，调用函数可以获取到局部变量
# def add(a):
#     a = 1
#     print(a)
#     return a
# #print(a)
# print(add())

#局部作用域能不能修改全局变量 不可以
#local variable 'a' referenced before assignment  局部变量没有赋值就引用了
a = "随风"
def add():
    #把a当初局部变量
    a = a + "王"
    return None
add()

#全局作用域能不能修改局部变量 不可以

#局部作用域声明为全局变量后能不能修改全局变量 可以
a = "随风"
def add():
    #把a当初局部变量
    global a
    a = a + "王"
    return None
add()