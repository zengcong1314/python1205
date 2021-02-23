import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('condition')


@pytest.mark.parametrize("info", data)
def test_condition(info):
    if "#register_name#" in info['url']:
        register_name = Handler.user_config['user']['register_name']
        info['url'] = info['url'].replace('#register_name#', register_name)
    if "#unregister_name#" in info['url']:
        unregister_name = Handler.generate_random_str(6)
        info['url'] = info['url'].replace('#unregister_name#', unregister_name)
    if "#register_email#" in info['url']:
        sql = 'select email from auth_user limit 1'
        result = Handler.db.query(sql)['email']
        info['url'] = info['url'].replace('#register_email#', result)
    if "#unregister_email#" in info['url']:
        unregister_email = Handler.generate_random_str(9)
        unregister_email = unregister_email + "@qq.com"
        info['url'] = info['url'].replace('#unregister_email#', unregister_email)
    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'])
    res_body = json.dumps(res.text)
    #assert json.loads(res.text)['count'] == info['expected']
    try:
        assert json.loads(res.text)['count'] == info['expected']
    except AssertionError as e:
        Handler.logger.error("用例失败：{}".format(e))
        raise e
    finally:
        # excel = ExcelHandler(excel_file)
        excel = Handler.excel
        excel.write('condition', str(res.text), row=int(info['case_id'] + 1), column=8)
        if json.loads(res.text)['count'] == info['expected']:
            excel.write('condition', True, row=int(info['case_id'] + 1), column=7)
        else:
            excel.write('condition', False, row=int(info['case_id'] + 1), column=7)