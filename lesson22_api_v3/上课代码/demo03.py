"""类和对象"""

class A:
    #一般都是需要的，存储代码，复用时绝大多情况下，数据是变化的，变化的数据提取为参数，
    # 在类里面变化的参数放在初始化函数里,
    # 需要对整个类传参数时，才用__init__，需要有变化的数据，通过不同的方法使用
    def __init__(self,param1,param2):
        pass

    def run(self):
        pass

class B(A):
    def run_abc(self):
        pass

# 怎么得到对象：实例化
a = A('a','b')
a.run()

b = A()

