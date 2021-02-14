import json

import pytest
import requests
from middleware.handler import Handler
# TODO:路径处理

data = Handler.excel.read_dict('register')
@pytest.mark.parametrize("test_info",data)
def test_register_01(test_info):
    if '#new_phone#' in test_info['json']:
        # 生成手机号码 13789456789 generate_new_phone
        mobile_phone = Handler.generate_new_phone()
    # 替换为new_phone
        test_info['json'] = test_info['json'].replace('#new_phone#',mobile_phone)
    # 通过这种方法，密码不一定知道，最好写入白名单
    if '#exist_phone#' in test_info['json']:
        pass
    # 传入都是字符串
    res = requests.request(method=test_info['method'],
                           url = Handler.yaml_config['host'] + test_info['url'],
                           headers = eval(test_info['headers']),
                           json=eval(test_info['json']))
    res_body = res.json()
    print(res_body)
    try:
        assert res_body['code'] == test_info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        excel = Handler.excel
        excel.write('register',
                    str(res_body),
                    row=int(test_info['case_id']) + 1,
                    column=9)
        if res_body['code'] == test_info['expected']:
            excel.write('register','True',row=int(test_info['case_id']) + 1,column=8)
        else:
            excel.write('register', 'False', row=int(test_info['case_id']) + 1, column=8)




