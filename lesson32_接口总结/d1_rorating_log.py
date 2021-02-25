import logging
import time
from logging import handlers
logger = logging.getLogger("python36")
# 初始化handler
handler = handlers.RotatingFileHandler('demo.log',
                                       maxBytes=100,
                                       backupCount=3,
                                       encoding='UTF-8')
logger.addHandler(handler)

# 打印日志
#logger.warning("生成警告信息{}".format(time.time()))
for i in range(100):
    logger.warning("生成警告信息{}".format(time.time()))
    time.sleep(0.1)
