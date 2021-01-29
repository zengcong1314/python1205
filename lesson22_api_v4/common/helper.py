"""帮助模块"""
import random

import faker

from common.db_handler import DBHandler


def generate_new_phone():
    """自动生成手机号"""
    fk = faker.Faker(locale='zh-CN')
    while True:
        phone = fk.phone_number()
        db = DBHandler()
        phone_in_db = db.query('select mobile_phone from member where mobile_phone={}'.format(phone))
        # 查询数据库
        # 如果数据库里面有这条记录，重新生成新的手机号码,循环，不知道什么时候结束，用while
        db.db_colse()
        if not phone_in_db:
            return phone
    return phone


# looker53.github.io 论坛

# 生成手机号码
def gen_mobile():
    """自动生成手机号"""
    while True:
        phone = '1' + random.choice(['3','5','7','8','9'])
        for i in range(9):
            num = random.randint(0,9)
            phone += str(num)

        #res = db.query('select * from future.loan where mobile_phone =={}'.format(phone))
        #if not res:
        return phone



if __name__ == '__main__':
    print(generate_new_phone())
    print(gen_mobile())
