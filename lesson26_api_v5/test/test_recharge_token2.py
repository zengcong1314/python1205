"""充值接口测试"""
import json
import os
import decimal

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
db = DBHandler()
sql = 'select leave_amount from member where id={}'.format(user_config['investor_user']['member_id'])
before_recharge_money = db.query(sql)
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
    res= requests.request(url= yaml_config['host'] + info['url'],
                     method=info['method'],
                     headers=headers,
                     json= json.loads(info['json']))
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

        after_recharge_money = db.query(sql)
        if json.loads(info["json"])['amount']:
            money = json.loads(info["json"])['amount']
        if res_body['code']== info["expected"]:
            excel.write('recharge',True,row=int(info['case_id']+1),column=8)
            if str(money).isdigit():
                if after_recharge_money['leave_amount'] == before_recharge_money['leave_amount'] + decimal.Decimal(money):
                    # float(after_recharge_money['leave_amount']) == float(before_recharge_money['leave_amount']) + float(money)
                    excel.write('recharge', "充值成功", row=int(info['case_id'] + 1), column=8)
        else:
            excel.write('recharge',False,row=int(info['case_id']+1),column=8)
