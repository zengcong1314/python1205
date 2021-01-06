# 对 logging 日志处理进行封装。使用 2 种方法：

# 方法一： 函数封装 def get_logger()
import logging
def get_logger(filename, level, msg):
    logger = logging.getLogger("zc36")
    logger.setLevel(level)

    file_handler = logging.FileHandler(filename, encoding="utf-8")
    file_handler.setLevel(level)

    handler = logging.StreamHandler()
    handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(handler)

    fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    file_handler.setFormatter(fmt)
    handler.setFormatter(fmt)

    if level == "DEBUG":
        logger.debug(msg)
    elif level == "INFO":
        logger.info(msg)
    elif level == "WARING":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)
    elif level == "CRITICAL":
        logger.critical(msg)

    logger.removeHandler(handler)

get_logger("zc.log","INFO","这是一条日志信息")


# 方法二： 类封装 class LoggerHander(logging.Logger)
class My_Log:
    def mylog(self,filename, level, msg):
        logger = logging.getLogger("zc36")
        logger.setLevel(level)

        file_handler = logging.FileHandler(filename, encoding="utf-8")
        file_handler.setLevel(level)

        handler = logging.StreamHandler()
        handler.setLevel(level)

        logger.addHandler(file_handler)
        logger.addHandler(handler)

        fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
        file_handler.setFormatter(fmt)
        handler.setFormatter(fmt)

        if level == "DEBUG":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "WARNING":
            logger.warning(msg)
        elif level == "error":
            logger.error(msg)
        elif level == "CRITICAL":
            logger.critical(msg)
        logger.removeHandler(handler)
mlog = My_Log()
mlog.mylog("zc1.log","INFO","这是一条完美得日志信息")

# 提示：得到收集器 logger 可以用 super()__init__ 哦！,   传入参数可以点击 Logger 类查看源码