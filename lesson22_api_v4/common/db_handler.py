from pymysql.cursors import DictCursor
import pymysql

class DBHandler:
    def __init__(self,
                 host='8.129.91.152',
                 port=3306,
                 user='future',
                 password='123456',
                 # 不要写成utf-8
                 charset='utf8',
                 database='futureloan',
                 cursorclass=DictCursor):

        self.conn = pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               # 不要写成utf-8
                               charset= charset,
                               database=database,
                               cursorclass=cursorclass)
        self.cursor = self.conn.cursor()

    def query_one(self,sql):
        # 'select * from futureloan.member limit 10;'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data
    def query_all(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def query(self,sql,one=True):
        self.cursor.execute(sql)
        if one:
            return  self.cursor.fetchone()
        return self.cursor.fetchall()

    def insert(self,sql):
        self.cursor.execute('insert')
        # 提交
        self.conn.commit()

    def db_colse(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    db=DBHandler()
    data=db.query('select * from futureloan.member limit 10;',one=False)
    print(data)
    db.db_colse()