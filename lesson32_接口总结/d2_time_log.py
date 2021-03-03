# 根据时间生成新文件
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('python36')
handler = TimedRotatingFileHandler('time12.log',when='s',interval=2,backupCount=100,encoding='UTF-8')
logger.addHandler(handler)

for i in range(100):
    logger.warning("生成警告信息{}".format(time.time()))
    time.sleep(0.1)

