import os
import re
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
    # yaml_path = os.path.join(config_path, 'config.yaml')
    # yaml_config = read_yaml(yaml_path)
    # print(yaml_config)
    # user_path = os.path.join(config_path, 'security.yaml')
    # user_config = read_yaml(user_path)
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
    app_id= ''
    app_id_copy = ''
    wsId = ''

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

    # 数据 需要动态替换 #。。。#的数据
    investor_phone = user_config['investor_user']['phone']
    investor_pwd = user_config['investor_user']['pwd']
    loan_phone = user_config['loan_user']['phone']
    loan_pwd = user_config['loan_user']['pwd']
    admin_phone = user_config['admin_user']['phone']
    admin_pwd = user_config['admin_user']['pwd']

    phone = user_config['investor_user']['phone']
    pwd = user_config['investor_user']['pwd']
    # def replace_data(self,string):
    #     import re
    #     res = re.finditer(r'#(.*?)#',string)
    #     for i in res:
    #         string = string.replace(i.group(),str(getattr(self,i.group(1))))
    #     return string
    @classmethod
    def replace_data(cls,string,pattern = '#(.*?)#'):
        """数据动态替换"""
        results = re.finditer(pattern=pattern, string=string)
        for result in results:
            print(result)
            # old='#investor_phone#'
            old_data = result.group()
            # key = 'investor_phone'
            key = result.group(1)
            new_data = str(getattr(cls, key, ''))
            string = string.replace(old_data, new_data)
        return string

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
    string = '{"mobile_phone":"#investor_phone#","pwd":"#investor_pwd#","mobile_phone":"#loan_phone#","pwd":"#loan_pwd#","mobile_phone":"#admin_phone#","pwd":"#admin_pwd#"}'
    a = Handler.replace_data(string)
    print(a)