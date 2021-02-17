import json

import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict('add')
@pytest.mark.parametrize("info", data)
def test_add_projects(info,login):
    if "#token#" in info['headers']:
        info['headers'] = info['headers'].replace('#token#',login['token'])
    if "#project_name#" in info['json']:
        project_name = Handler.generate_random_str(6)
        info['json'] = info['json'].replace('#project_name#',project_name)
    if "*project_name*" in info['json']:
        project_name = Handler.user_config['user']['project_name']
        info['json'] = info['json'].replace('*project_name*',project_name)
    res = requests.request(method=info['method'],
                           url=Handler.yaml_config['host'] + info['url'],
                           headers=json.loads(info['headers']),
                           json=json.loads(info['json']))
    assert res.status_code == info['expected']