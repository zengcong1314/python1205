"""
直接使用logging 有以下问题：
- info信息没有产生
- 文件输出日志
- 时间，运行日志的位置

最好不要直接用 logging.info这样的操作
学习的时候：帮助我们理解logging 的概念
1、noset 0 等于没写，废话
2、debug 10 调试 一些额外信息，备注，往往和主体功能无关，日报里面得备注
3、info,20 主体 功能得信息，日报，做了些啥
4、warning 30 警告 下次可能要出错了，交警叔叔警告
5、error 40 犯错，违法 抢红灯
6、critical 50 极其严重 抢银行
默认记录warning以上等级

"""
import logging
class Dog():

    def __init__(self,color):
        logging.info("正在初始化。。。")
        self.color = color
        logging.info("获取属性color")
        self.ke = "dog"
        logging.warning("警告。。")
        try:
            a = []
            a[100]
        except IndexError:
            logging.error("超出异常错误，这里有错误，赶紧来处理！！！")

    def run(self):
        print("狗再跑")

dog = Dog("黑色")
