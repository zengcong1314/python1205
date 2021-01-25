"""日志处理器的封装"""
#导入信息放在模块的最上面
import logging
import os

from config import path


def get_log(logname="root",
            logger_level="DEBUG",
            stream_handler_level="DEBUG",
            file=None,file_handler_level="DEBUG",
            fmt_str="time: %(asctime)s---%(levelname)s:%(name)s:%(message)s---%(filename)s---%(lineno)s"):
    """logging封装"""

    # 获取日志收集器 logger
    logger = logging.getLogger(logname)
    logger.setLevel(logger_level)
    # 设置格式"time: %(asctime)s---%(levelname)s:%(name)s:%(message)s---%(filename)s---%(lineno)s"
    fmt = logging.Formatter(fmt_str)

    # 日志处理器(输出到控制台上)
    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)
    # 处理器添加到收集器上
    logger.addHandler(handler)
    handler.setFormatter(fmt)

    # 文件处理器
    if file:
        file_handler = logging.FileHandler(file, encoding="utf-8")
        file_handler.setLevel(file_handler_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)

    return logger

log_file = os.path.join(path.logs_path,'demo.txt')
print(log_file)
# 收集器
logger = get_log(file=log_file)

if __name__ == '__main__':
    log1 = get_log(file="zc.log")
    #不要调用两次get_log()
    log1.info("这是一条日志信息")
    #get_log(file="zc.log").error("错误")
    log1.error("这是一条错误日志")


