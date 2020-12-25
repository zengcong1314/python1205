"""

except:异常类型：捕获指定类型的异常

"""
a = 3
b = 0
try:
    a / b
except Exception as e:
    print(e)
    print("b不能为0")

print("无论如何都会执行")

