"""
1、日志收集器logger
2、日志收集器级别 level
3、日志处理器准备handler  展示出来
4、日志处理器级别设置  展示
5、设置日志格式 format
6、添加日志处理器
"""
import logging

# 获取日志收集器 logger
logger = logging.getLogger("python36")
logger.setLevel("INFO")

# 日志处理器(输出到控制台上)
handler = logging.StreamHandler()
handler.setLevel("INFO")

# 文件处理器
file_handler = logging.FileHandler("python36.log",encoding="utf-8")
file_handler.setLevel("INFO")

# 处理器添加到收集器上
logger.addHandler(handler)
logger.addHandler(file_handler)

#设置格式
fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

logger.info("正常执行得逻辑")
logger.error("错误")
logger.debug("调试信息")




