#导入信息放在模块的最上面
import logging
class MY_Log(logging.Logger):
    # pass
    def __init__(self,logname="root",
                 logger_level="DEBUG",
                 stream_handler_level="DEBUG",
                 file=None,
                 file_handler_level="DEBUG",
                 fmt_str="time: %(asctime)s---%(levelname)s:%(name)s:%(message)s---%(filename)s---%(lineno)s"):

        # 获取日志收集器 logger
        super().__init__(logname,logger_level)
        # self == 收集器
        #self.logger = logger
        #self.logger.setLevel(logger_level)
        self.setLevel(logger_level)
        # 设置格式"time: %(asctime)s---%(levelname)s:%(name)s:%(message)s---%(filename)s---%(lineno)s"
        fmt = logging.Formatter(fmt_str)
    #
        # 日志处理器(输出到控制台上
        handler = logging.StreamHandler()
        handler.setLevel(stream_handler_level)
        # 处理器添加到收集器上
        self.addHandler(handler)
        handler.setFormatter(fmt)

        # 文件处理器
        if file:
            file_handler = logging.FileHandler(file, encoding="utf-8")
            file_handler.setLevel(file_handler_level)
            self.addHandler(file_handler)
            file_handler.setFormatter(fmt)



if __name__ == '__main__':
    log1 = MY_Log("zc.log")
    #不要调用两次get_log()
    log1.info("这是一条日志信息")
    #get_log(file="zc.log").error("错误")
    log1.error("这是一条错误日志")



