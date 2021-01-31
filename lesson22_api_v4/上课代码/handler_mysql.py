import pymysql
class db_handler():
    def __init__(self,host,port,user,pwd):
        self.host=host
        self.port=port
        self.user=user
        self.pwd=pwd


    def query(self,sql,one=False):
        #conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, charset='utf8', port=self.port)
        conn=pymysql.connect(self.host,self.user,self.pwd,None,self.port,charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql)
        if not one:
            return  cursor.fetchall()
        return cursor.fetchone()

if __name__ == '__main__':
    host='8.129.91.152'
    port=3306
    user='future'
    pwd='123456'
    db = db_handler(host,port,user,pwd)
    sql='select * from futureloan.member limit 10;'
    print(db.query(sql))

