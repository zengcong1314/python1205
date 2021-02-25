import pymysql
from pymysql.cursors import DictCursor


class DBHandler:
    def __init__(self,
                 host='www.keyou.site',
                 port=13306,
                 user='lemon520',
                 password='123456',
                 charset='utf8',
                 database='test',
                 cursorclass=DictCursor):

        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    charset=charset,
                                    database=database,
                                    cursorclass=cursorclass)


    def query(self,sql,one=True):
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.execute(sql)
        if one:
            self.cursor.close()
            return self.cursor.fetchone()
        self.cursor.close()
        return self.cursor.fetchall()

    def db_colse(self):
        self.conn.close()

if __name__ == '__main__':
    db=DBHandler()
    data=db.query('select * from test.auth_user',one=False)
    print(data)
    db.db_colse()