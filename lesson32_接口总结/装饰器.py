# 装饰器 @装饰器函数 增强函数功能，用函数调函数  本质就是一个高阶函数，以一个函数作为参数放到另一个函数里，返回一个函数的高阶函数。
#以一个函数作为参数放到另一个函数里，返回值也是一个函数
# 修饰函数，扩展原有函数功能
# 1、代码变得美观、优雅 2、扩展函数功能 高阶函数
# 装饰器可以带参数，可以用在类里面

# 一个最简单的装饰器

# def run(func):
#     print("hello")
#     return func
#
# res = run(max)
# print(res)
# print(max(3,4,5))
# print(res(3,4,5))

# if __name__ == '__main__':
#     res = run('demo')
    #print(res)
import time


# def run():
#     print("正在运行")
# 装饰器
def log_time(func):

    def wrapper():
        print(time.time())
        func()
        return 2

    return wrapper

@log_time
def run():
    print("正在运行")

run()

# @classmethod
# @pytest.mark
# @pytest.fixture


