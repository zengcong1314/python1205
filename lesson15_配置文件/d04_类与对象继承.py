class Logger:
    def __init__(self,name):
        print("正在初始化收集器")
        self.name = name

    def info(self,msg):
        print("正在记录msg")

class MyLogger(Logger):
    def __init__(self,name,fmt,level):
        super().__init__(name)
        pass

log = MyLogger("hello","debug","fow")
log.info("hello")