import logging

def get_log(name="root",
            logger_level="DEBUG",
            stream_handler_level="DEBUG",
            file=None,file_handler_lever="DEBUG",
            fmt_str="time: %(asctime)s---%(levelname)s:%(name)s:%(message)s---%(filename)s---%(lineno)s"):
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)

    fmt = logging.Formatter(fmt_str)

    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)

    logger.addHandler(handler)
    handler.setFormatter(fmt)

    if file:
        file_handler = logging.FileHandler(file,encoding="utf-8")
        file_handler.setLevel(file_handler_lever)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger

if __name__ == '__main__':
    log = get_log(file="zc.log")
    log.info("这是一条日志信息")
    log.error("这是一条错误信息")