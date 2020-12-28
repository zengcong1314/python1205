
import random

from locust import TaskSet,HttpLocust,task,between

#定义一个任务类，这个类名称自己随便定义，类继承TaskSequence 或TaskSet类，所以要从locust中，引入TaskeSequence或TaskSet
#当类里面的任务请求有先后顺序后，继承TaskSequence，没有先后顺序，可以使用继承TaskSet类
class MyTaskCase(TaskSet):
    #初始化方法，相当于 setup
    def on_start(self):
        pass

    #@task python中的装饰器，告诉下面的方法是一个任务，任务就可以是一个接口请求，
    # 这个装饰器和下面的方法被复制多次，改动一下，就能写出多个接口
    # 装饰器后面带上（数字）代表在所有任务中，执行比例
    # 要用这个装饰器，需要头部引入 从locust中，引入 task

    @task
    @seq_task(1) #装饰器，定义有执行顺序的任务，扩展中的数字，从小到大，代表先后执行顺序
    def regist_(self): # 一个方法，方法名称可以自己改
        url = '/erp/regist' #接口请求的URL地址
        self.headers = {"Content-Type":"application/json"} # 定义请求头为类变量，这样其他任务也可以调用该变量

