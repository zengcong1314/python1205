"""帮助模块"""
import random

import faker



def generate_new_phone():
    """自动生成手机号"""
    fk = faker.Faker(locale='zh-CN')
    phone = fk.phone_number()
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
