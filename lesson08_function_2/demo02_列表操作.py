dalao = ["呦呦呦","wen"]

#调用这两个函数为什么返回None，因为函数定义时没有返回值
# print(dalao.append("不变的音乐")) #append是函数，打印函数调用的过程，打印出来的是函数返回值，没有返回值时，默认None
#
# print(dalao.remove("wen"))  #和函数返回值有关系
#
# print(dalao)

b = dalao.append("不变得音乐")#用变量接收与不用变量区别，没区别 append函数的返回值为None，定义的时候返回值为None，永远为None
print(b)

c = dalao.pop(0) #因为函数定义的时候有返回值，源代码是用C写的，我们看不到
print(c)

#函数你调用的时候得到的值是由返回值决定的