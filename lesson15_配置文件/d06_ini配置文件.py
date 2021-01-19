"""
ini是传统的主流配置文件
支持的数据类型不多，所有的值都默认当成了字符串
- [],section,分组
- option ,获取某个option，必须通过section
"""
from configparser import ConfigParser

#初始化一个解析对象
parser = ConfigParser()

#解析对象读取文件
parser.read("python36.ini",encoding="UTF-8")

# 获取某个配置
host = parser.get("default","host")
db_host = parser.get("db","host")

print(host)
print(db_host)

# 获取端口
port = parser.get('db','port')
print(port)
