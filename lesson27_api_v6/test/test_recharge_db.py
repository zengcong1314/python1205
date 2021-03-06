"""充值接口测试"""
import json
import os
import decimal
from decimal import Decimal

import pytest
import requests
from common.excel_handler import ExcelHandler
from config.path import data_path
from common.yaml_handler import yaml_config,user_config
from common.logger_hander import logger
from common.helper import generate_new_phone
from common.db_handler import DBHandler

excel_file = os.path.join(data_path,'demo.xlsx')
data = ExcelHandler(excel_file).read_dict('recharge')
print(data)

#db.db_colse()
@pytest.mark.parametrize('info',data)
def test_recharge(info,login):
    """充值"""
    """先要替换"""
    if "#member_id#" in info['json']:
        info["json"] = info["json"].replace('#member_id#',str(login['id']))
    if "#wrong_member_id#" in info['json']:
        info["json"] = info["json"].replace('#wrong_member_id#', str(login['id'] + 1))

    # # token组装方式1：通过excel替换
    # if "#token#" in info['headers']:
    #     info["headers"] = info["headers"].replace("#token#",login['token'])

    # token 组装2：通过headers 添加,excel 表格里面不需要Authorization
    headers = json.loads(info["headers"])
    headers['Authorization'] = login['token']

    # 数据库访问，充值之前的余额
    db = DBHandler()
    sql = 'select leave_amount from member where id={}'.format(login['id'])
    result = db.query(sql)
    before_recharge_money =result['leave_amount']
    db.db_colse()

    data = json.loads(info['json'])
    res= requests.request(url= yaml_config['host'] + info['url'],
                     method=info['method'],
                     headers=headers,
                     json= data)
    res_body = res.json()
    print(res_body)
    try:
        assert res_body['code'] == info["expected"]
    except AssertionError as e:
        logger.error("用例失败：{}".format(e))
        raise e
    finally:
        excel = ExcelHandler(excel_file)
        excel.write('recharge',str(res_body),row=int(info['case_id']+1),column=9)
        if res_body['code'] == 0:
            db = DBHandler()
            sql = 'select leave_amount from member where id={}'.format(login['id'])
            result = db.query(sql)
            after_recharge_money = result['leave_amount']
            db.db_colse()
            money = Decimal(str(data['amount']))
            assert before_recharge_money + money == after_recharge_money
        if res_body['code'] == info["expected"]:
            excel.write('recharge',True,row=int(info['case_id']+1),column=8)
        else:
            excel.write('recharge',False,row=int(info['case_id']+1),column=8)
