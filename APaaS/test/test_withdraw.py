import json
import os
import pytest
import requests
import decimal
from common.excel_handler import ExcelHandler
from config.path import data_path
from middleware.handler import Handler

# excel_file = os.path.join(data_path,'demo.xlsx')
data = Handler.excel.read_dict('withdraw')
print(data)

@pytest.mark.parametrize("info",data)
def test_withdraw(info,login_investor,db):
    # db = DBHandler()
    Handler.inverstor_user_id = login_investor['id']
    Handler.inverstor_user_token = login_investor['token']

    sql = 'select leave_amount from member where id={}'.format(login_investor['id'])
    before_withdraw_money = Handler.db.query(sql)['leave_amount']
    # Handler.new_phone = Handler.generate_new_phone()
    if "#member_id#" in info['json']:
        info["json"] = info["json"].replace("#member_id#",str(login_investor['id']))
    if "#wrong_member_id#" in info['json']:
        info["json"] = info["json"].replace('#wrong_member_id#', str(login_investor['id'] + 10))
    if "#amount#" in info["json"]:
        info["json"] = info["json"].replace('#amount#',str(before_withdraw_money + 1))

    headers=json.loads(info['headers'])
    headers['Authorization']=login_investor['token']

    res = requests.request(method=info['method'],
                     url=Handler.yaml_config['host'] + info['url'],
                     headers=headers,
                     json=json.loads(info['json']))
    res_body = res.json()
    try:
        assert res_body['code'] == info["expected"]
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        excel = Handler.excel
        excel.write('withdraw',str(res_body),row=int(info['case_id']+1),column=9)
        after_withdraw_money = Handler.db.query(sql)['leave_amount']
        if json.loads(info["json"])['amount']:
            money = json.loads(info["json"])['amount']
        if res_body['code']== 0:
            #try:
                assert float(after_withdraw_money) == float(before_withdraw_money) - float(money)
            #except AssertionError as e:
                #raise e
        if res_body['code'] == info["expected"]:
            excel.write('withdraw',True,row=int(info['case_id']+1),column=8)
        else:
            excel.write('withdraw',False,row=int(info['case_id']+1),column=8)
