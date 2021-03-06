import os

import faker
from pymysql.cursors import DictCursor
#from common import helper
from common.logger_hander import get_log
from common.yaml_handler import read_yaml
from config import path
from config.path import config_path
from common.excel_handler import ExcelHandler
from common.db_handler import DBHandler

yaml_path = os.path.join(config_path, 'config.yaml')
yaml_config = read_yaml(yaml_path)
print(yaml_config)
user_path = os.path.join(config_path, 'security.yaml')
user_config = read_yaml(user_path)

# class MidDBHanlder(DBHandler):
#     def __init__(self, host=user_config['db']['host'],
#                        port=user_config['db']['port'],
#                        user=user_config['db']['user'],
#                        password=user_config['db']['password'],
#                        # 不要写成utf-8
#                        charset=user_config['db']['charset'],
#                        database=user_config['db']['database'],
#                        cursorclass=DictCursor):
#         super.__init__(host=host,
#                        port=port,
#                        user=user,
#                        password=password,
#                        charset=charset,
#                        database=database,
#                        cursorclass=cursorclass)

class MidDBHanlder(DBHandler):

    def __init__(self):
        super().__init__(host=user_config['db']['host'],
                       port=user_config['db']['port'],
                       user=user_config['db']['user'],
                       password=user_config['db']['password'],
                       # 不要写成utf-8
                       charset=user_config['db']['charset'],
                       database=user_config['db']['database'],
                       cursorclass=DictCursor)
class Handler():
    """任务：中间层。common 和 调用层。
    使用项目得配置数据，填充common模块
    """
    new_phone = ''
    inverstor_user_id = ''
    inverstor_user_token = ''
    admin_user_id = ''
    admin_user_token = ''
    loan_user_id = ''
    loan_user_token = ''

    yaml_path = os.path.join(config_path, 'config.yaml')
    yaml_config = read_yaml(yaml_path)
    print(yaml_config)
    user_path = os.path.join(config_path, 'security.yaml')
    user_config = read_yaml(user_path)

    # logger
    log_file = os.path.join(path.logs_path, yaml_config['logger']['file'])
    logger = get_log(name=yaml_config['logger']['name'],
                     file=log_file)

    # excel对象
    excel_file = os.path.join(path.data_path, 'demo.xlsx')
    excel = ExcelHandler(excel_file)

    # 新手机号码
    new_phone = ''
    @classmethod
    def generate_new_phone(cls):
        """自动生成手机号"""
        fk = faker.Faker(locale='zh-CN')
        while True:
            phone = fk.phone_number()
            db2 = Handler.db
            phone_in_db = db2.query('select mobile_phone from member where mobile_phone={}'.format(phone))
            # 查询数据库
            # 如果数据库里面有这条记录，重新生成新的手机号码,循环，不知道什么时候结束，用while
            #db2.db_colse()
            if not phone_in_db:
                cls.new_phone = phone
                return phone
        return phone

    # 数据库
    # db = DBHandler(host=user_config['db']['host'],
    #                port=user_config['db']['port'],
    #                user=user_config['db']['user'],
    #                password=user_config['db']['password'],
    #                # 不要写成utf-8
    #                charset=user_config['db']['charset'],
    #                database=user_config['db']['database'],
    #                cursorclass=DictCursor)
    # 数据库
    db = MidDBHanlder()
    db_class = MidDBHanlder
if __name__ == '__main__':
    Handler.logger.warning("可以正常使用吗？？")
    h = Handler()
    h.logger.warning("还可以吗")