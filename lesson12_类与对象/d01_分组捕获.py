"""
分组捕获
异常也可以分组
"""
a = 3
b = 0
try:
    # 可能发生异常的代码
    [1,2][100]
    a / b


except (ZeroDivisionError,IndexError) as e:
    print(e)
    print("记录日志")
except (KeyError,ValueError) as e:
    print("赶紧联系开发")
# except IndexError as err:
#     print(err)
#     print("赶紧练习开发。")
finally:
    #无论如何都会执行，不管有没有捕获到 except
    #文件，关闭
    print("无论如何都会执行")

with open("file") as f:
    pass

try:
    f = open()
except:
    #错误逻辑
    pass
else:
    #当except没有被触发的时候
    #会执行的代码
    pass
finally:
    f.close()