"""mysql,oracle,sql-server,postgres,redis,mongodb
mariadb
安装
pymysql
"""
import pymysql

# 1.建立连接
conn = pymysql.connect(host='8.129.91.152',
                       port=3306,
                       user='future',
                       password='123456',
                       # 不要写成utf-8
                       charset='utf8',
                       database='futureloan'
                       )
# 2.获取游标
cursor = conn.cursor()
# 3.通过游标执行SQL语句
cursor.execute('select * from futureloan.member where id={} limit 10;'.format(1))
# 4.通过游标得到结果
data1 = cursor.fetchall()
print(data1)
# data2 = cursor.fetchone()
# print(data2)

# 数据库，请用类封装
