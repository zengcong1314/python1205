import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('register')
@pytest.mark.parametrize("info",data)
def test_register_01(info):
    if "#new_username#"  in info['json']:
        username = Handler.generate_random_str(6)
        info['json'] = info['json'].replace('#new_username#',username)
    if "#old_username#"  in info['json']:
        username = Handler.user_config['user']['login_user']
        info['json'] = info['json'].replace('#old_username#',username)
    if "#email#" in info['json']:
        email = Handler.generate_random_str(9)
        email = email + "@qq.com"
        info['json'] = info['json'].replace('#email#',email)
    if "*email*" in info['json']:
        sql = 'select email from auth_user limit 1'
        email = Handler.db.query(sql)['email']
        #email = email + "@qq.com"
        #info['url'] = info['url'].replace('#register_email#', result)
        info['json'] = info['json'].replace('*email*', email)

    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'],
                           json=json.loads(info['json']))
    #assert res.status_code ==info['expected']
    try:
        assert res.status_code == info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('register', str(res.text), row=int(info['case_id'] + 1), column=8)
        if res.status_code == info['expected']:
            excel.write('register', True, row=int(info['case_id'] + 1), column=7)
        else:
            excel.write('register', False, row=int(info['case_id'] + 1), column=7)