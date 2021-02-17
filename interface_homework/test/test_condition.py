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
        register_email = Handler.user_config['user']['register_email']
        info['url'] = info['url'].replace('#register_email#', register_email)
    if "#unregister_email#" in info['url']:
        unregister_email = Handler.generate_random_str(9)
        unregister_email = unregister_email + "@qq.com"
        info['url'] = info['url'].replace('#unregister_email#', unregister_email)
    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'])
    res_body = json.dumps(res.text)
    assert json.loads(res.text)['count'] == info['expected']