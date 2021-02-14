import json
import os
import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('login')
@pytest.mark.parametrize('info',data)
def test_login (info):
    all_data = json.dumps(info)
    # 替换
    info = Handler.replace_data(all_data)
    print(info)
    # 转化成字典
    info = json.loads(info)
    Handler.new_phone = Handler.generate_new_phone()

    if '*phone*' in info['json']:
        mobile_phone =Handler().generate_new_phone()
        info['json'] = info['json'].replace('*phone*',mobile_phone)

    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'],
                           headers=json.loads(info['headers']),
                           json=json.loads(info['json']))
    res_body = res.json()

    try:
        assert res_body['code'] == info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        #excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('login',str(res_body),row=int(info['case_id']+1),column=9)
        if res_body['code']== info['expected']:
            excel.write('login',True,row=int(info['case_id']+1),column=8)
        else:
            excel.write('login',False,row=int(info['case_id']+1),column=8)


