import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('login')


@pytest.mark.parametrize("info", data)
def test_login(info):
    if "*username*" in info['json']:
        username = Handler.generate_random_str(6)
        info['json'] = info['json'].replace('*username*', username)
    if "#username#" in info['json']:
        username = Handler.user_config['user']['login_user']
        info['json'] = info['json'].replace('#username#', username)
    if "#pwd#" in info['json']:
        pwd = Handler.user_config['user']['password']
        info['json'] = info['json'].replace('#pwd#', pwd)
    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'],
                           json=json.loads(info['json']))
    #assert res.status_code == info['expected']

    try:
        assert res.status_code == info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('login', str(res.text), row=int(info['case_id'] + 1), column=8)
        if res.status_code == info['expected']:
            excel.write('login', True, row=int(info['case_id'] + 1), column=7)
        else:
            excel.write('login', False, row=int(info['case_id'] + 1), column=7)