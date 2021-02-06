import os
import pytest
import requests
from middleware.handler import Handler
# from common.yaml_handler import yaml_config,user_config
# from common.logger_hander import logger
# from common.helper import generate_new_phone
# from common.excel_handler import ExcelHandler
# from config.path import data_path

# excel_file = os.path.join(data_path,'demo.xlsx')
# data = ExcelHandler(excel_file).read_dict('login')
data = Handler.excel.read_dict('login')
@pytest.mark.parametrize('test_info',data)
def test_login (test_info):
    actual_url = test_info['url']
    actual_method = test_info['method']
    actual_json = test_info['json']
    actual_headers = test_info['headers']
    expected = test_info['expected']

    if '*phone*' in actual_json:
        mobile_phone =Handler().generate_new_phone()
        actual_json = actual_json.replace('*phone*',mobile_phone)
    if '#phone#' in actual_json:
        mobile_phone =Handler.user_config['investor_user']['phone']
        actual_json = actual_json.replace('#phone#',mobile_phone)
    if '#pwd#' in actual_json:
        pwd =Handler.user_config['investor_user']['pwd']
        actual_json = actual_json.replace('#pwd#',pwd)
    print(actual_json)
    res = requests.request(method=actual_method,
                           url=Handler.yaml_config['host'] + actual_url,
                           headers=eval(actual_headers),
                           json=eval(actual_json))
    res_body = res.json()

    try:
        assert res_body['code'] == expected
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        #excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('login',str(res_body),row=int(test_info['case_id']+1),column=9)
        if res_body['code']== expected:
            excel.write('login',True,row=int(test_info['case_id']+1),column=8)
        else:
            excel.write('login',False,row=int(test_info['case_id']+1),column=8)


