"""
在一个函数当中，能不能调用本身。
可以调用其他函数吗
我先找一下这个文件当中有哪些函数，顶格写的
"""

def get_offer(name,money,food):
    """获取offer"""
    print("{}拿到了一个{}k的offer".format(name,money))
    eat(name,food) #这里是实际参数
def eat(eta_name,eat_food):
    print("{}最喜欢吃{}".format(eta_name,eat_food))

get_offer("旧梦",23,"辣条")

#name = "旧梦"
#eat_name = name
#eat_name = "旧梦"

