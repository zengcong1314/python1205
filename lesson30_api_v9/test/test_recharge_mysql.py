"""充值接口测试"""
import json
import os
import decimal
from decimal import Decimal

import pytest
import requests
from middleware.handler import Handler
# from common.yaml_handler import yaml_config,user_config
# # from common.logger_hander import logger
# from common.helper import generate_new_phone
# from common.db_handler import DBHandler
# from common.excel_handler import ExcelHandler
# from config.path import data_path

# excel_file = os.path.join(data_path,'demo.xlsx')
# data = ExcelHandler(excel_file).read_dict('recharge')
data = Handler.excel.read_dict("recharge")
# data = Handler.excel.read_dict("recharge")[4:] 切片来调试
print(data)

#db.db_colse()
@pytest.mark.parametrize('info',data)
def test_recharge(info,login_investor,db):
    """充值"""
    """先要替换"""
    Handler.inverstor_user_id = login_investor['id']
    Handler.inverstor_user_token = login_investor['token']

    if "#member_id#" in info['json']:
        info["json"] = info["json"].replace('#member_id#',str(login_investor['id']))
    if "#wrong_member_id#" in info['json']:
        info["json"] = info["json"].replace('#wrong_member_id#', str(login_investor['id'] + 1))

    # token 组装2：通过headers 添加,excel 表格里面不需要Authorization
    headers = json.loads(info["headers"])
    headers['Authorization'] = login_investor['token']

    # 数据库访问，充值之前的余额
    # db = DBHandler()
    sql = 'select leave_amount from member where id={}'.format(login_investor['id'])
    result = Handler.db.query(sql)
    before_recharge_money =result['leave_amount']
    # db.db_colse()

    data = json.loads(info['json'])
    res= requests.request(url= Handler.yaml_config['host'] + info['url'],
                     method=info['method'],
                     headers=headers,
                     json= data)
    res_body = res.json()
    print(res_body)
    try:
        assert res_body['code'] == info["expected"]
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('recharge',str(res_body),row=int(info['case_id']+1),column=9)
        if res_body['code'] == 0:
            # db = DBHandler()
            sql = 'select leave_amount from member where id={}'.format(login_investor['id'])
            result = Handler.db.query(sql)
            after_recharge_money = result['leave_amount']
            # db.db_colse()
            money = Decimal(str(data['amount']))
            try:
                assert before_recharge_money + money == after_recharge_money
            except AssertionError as e:
                raise e
        if res_body['code'] == info["expected"]:
            excel.write('recharge',True,row=int(info['case_id']+1),column=8)
        else:
            excel.write('recharge',False,row=int(info['case_id']+1),column=8)
