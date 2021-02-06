"""充值接口测试"""
import json
import os
import pytest
import requests
from common.excel_handler import ExcelHandler
from config.path import data_path
from common.yaml_handler import yaml_config,user_config
from common.logger_hander import logger
from common.helper import generate_new_phone

excel_file = os.path.join(data_path,'demo.xlsx')
data = ExcelHandler(excel_file).read_dict('recharge')
print(data)
@pytest.mark.parametrize('info',data)
def test_recharge(info,login):
    """充值"""
    """先要替换"""
    if "#member_id#" in info['json']:
        info["json"] = info["json"].replace('#member_id#',str(login['id']))
    if "#wrong_member_id#" in info['json']:
        info["json"] = info["json"].replace('#wrong_member_id#', str(login['id'] + 1))

    # token组装方式1：通过excel替换
    if "#token#" in info['headers']:
        info["headers"] = info["headers"].replace("#token#",login['token'])

    res= requests.request(url= yaml_config['host'] + info['url'],
                     method=info['method'],
                     headers=json.loads(info['headers']),
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
        if res_body['code']== info["expected"]:
            excel.write('recharge',True,row=int(info['case_id']+1),column=8)
        else:
            excel.write('recharge',False,row=int(info['case_id']+1),column=8)
