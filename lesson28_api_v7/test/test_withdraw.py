import json
import os
import pytest
import requests
import decimal
from common.excel_handler import ExcelHandler
from config.path import data_path
from common.yaml_handler import yaml_config,user_config
from common.logger_hander import logger
from common.db_handler import DBHandler
from middleware.handler import Handler

excel_file = os.path.join(data_path,'demo.xlsx')
data = ExcelHandler(excel_file).read_dict('withdraw')
db = DBHandler()
sql = 'select leave_amount from member where id={}'.format(user_config['investor_user']['member_id'])
before_recharge_money = db.query(sql)['leave_amount']
@pytest.mark.parametrize("info",data)
def test_withdraw(info,login_investor):
    Handler.new_phone = Handler.generate_new_phone()
    if "#member_id#" in info['json']:
        info["json"] = info["json"].replace("#member_id#",str(login_investor['id']))
    if "#wrong_member_id#" in info['json']:
        info["json"] = info["json"].replace('#wrong_member_id#', str(login_investor['id'] + 10))
    if "#amount#" in info["json"]:
        info["json"] = info["json"].replace('#amount#',str(before_recharge_money + 1))

    headers=json.loads(info['headers'])
    headers['Authorization']=login_investor['token']
    res = requests.request(method=info['method'],
                     url=yaml_config['host'] + info['url'],
                     headers=headers,
                     json=json.loads(info['json']))
    res_body = res.json()
    try:
        assert res_body['code'] == info["expected"]
    except AssertionError as e:
        logger.error("用例失败：{}".format(e))
        raise e
    finally:
        excel = ExcelHandler(excel_file)
        excel.write('withdraw',str(res_body),row=int(info['case_id']+1),column=9)
        after_recharge_money = db.query(sql)['leave_amount']
        if json.loads(info["json"])['amount']:
            money = json.loads(info["json"])['amount']
        if res_body['code']== info["expected"]:
            excel.write('withdraw',True,row=int(info['case_id']+1),column=8)
            if str(money).isdigit():
                # if after_recharge_money == before_recharge_money - decimal.Decimal(money):
                if float(after_recharge_money) == float(before_recharge_money) - float(money):
                    excel.write('withdraw', "充值成功", row=int(info['case_id'] + 1), column=8)
        else:
            excel.write('withdraw',False,row=int(info['case_id']+1),column=8)
