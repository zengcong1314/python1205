import os
import re
import random
import string
from pymysql.cursors import DictCursor
from common.yaml_handler import read_yaml
from config import path
from common.db_handler import DBHandler
from common.logger_handler import get_log
from common.excel_handler import ExcelHandler



yaml_path = os.path.join(path.config_path,'config.yaml')
yaml_config = read_yaml(yaml_path)
user_path = os.path.join(path.config_path,'security.yaml')
user_config = read_yaml(user_path)

class MidDBHandler(DBHandler):
    def __init__(self):
        super().__init__(host=user_config['db']['host'],
                         port=user_config['db']['port'],
                         user=user_config['db']['user'],
                         password=user_config['db']['password'],
                         charset=user_config['db']['charset'],
                         database=user_config['db']['database'],
                         cursorclass=DictCursor)

class Handler():
    yaml_path = os.path.join(path.config_path, 'config.yaml')
    yaml_config = read_yaml(yaml_path)
    user_path = os.path.join(path.config_path, 'security.yaml')
    user_config = read_yaml(user_path)

    log_file = os.path.join(path.logs_path,yaml_config['logger']['file'])
    logger = get_log(name=yaml_config['logger']['name'],
                     file=log_file)

    excel_file = os.path.join(path.data_path,'demo.xlsx')
    excel = ExcelHandler(excel_file)



    def generate_random_str(randomlength=16):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str

    db = MidDBHandler()


