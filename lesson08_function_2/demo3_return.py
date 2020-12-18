"""
1、return 决定返回值
2、函数遇到return 就会终止
"""

def add(a,b):
    c = a + b
    d = c * a
    e = d * b
    print("before finished")
    if d < 3:
        return "1"
    print("2")
    return "5"
    #break
    print("hello world")
    print("yuz")

b = add(3,4) #函数返回值是return 5,所以 b = 5
#TODO：没有print，return值就不会出现在屏幕上
print(b)

c = add(1,1)
print(c)