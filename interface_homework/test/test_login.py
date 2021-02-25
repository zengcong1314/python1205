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
    assert res.status_code == info['expected']