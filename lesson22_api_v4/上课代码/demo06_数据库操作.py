"""mysql,oracle,sql-server,postgres,redis,mongodb
mariadb
安装
pymysql
"""
import pymysql

# 1.建立连接
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       # 不要写成utf-8
                       charset='utf8',
                       database='futureloan',
                       cursorclass=DictCursor
                       )
# 2.获取游标
cursor = conn.cursor(DictCursor)
# 3.通过游标执行SQL语句
# cursor.execute('select * from futureloan.member where id={} limit 10;'.format(1))
cursor.execute('select * from futureloan.member  limit 10;')
# 4.通过游标得到结果

data2 = cursor.fetchone()
print(data2)
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from futureloan.member  limit 10;')
data1 = cursor.fetchall()
print(len(data1))

# 关闭
# 1.先关闭游标
cursor.close()
# 2.关闭链接
conn.close()

# 数据库，请用类封装
#
