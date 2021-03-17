import json

from jsonpath import jsonpath
import requests
from middleware.handler import Handler
import pytest

data = Handler.excel.read_dict('app')

@pytest.mark.parametrize("info",data)
def test_add_app(info,login):
    headers = {}
    headers['Authorization'] = login['tokenType'] + ' ' + login['accessToken']
    print(headers)

    if info['method'] == 'get':
        res = requests.request(method=info["method"],
                               url=Handler.yaml_config['host'] + info['url'],
                               headers=headers)
    else:
        res = requests.request(method=info["method"],
                               url=Handler.yaml_config['host'] + info['url'],
                               headers=headers,
                               json=json.loads(info["json"]))


    print(res.json())
    assert res.json()['code'] == info['expected']


