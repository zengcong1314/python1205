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
    # info 取出来是字典，转化为字符串
    all_data = json.dumps(info)
    # 字符串替换
    info = Handler.replace_data(all_data)
    print(info)
    # 字符串转化成字典
    info = json.loads(info)

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
    # 设置Handler对应的属性
    if info['extractor']:
        extrators = json.loads(info['extractor'])
        for prop,jsonpath_exp in extrators.items():
            # value = 'id'
            value = jsonpath(res.json(),jsonpath_exp)[0]
            # setattr(Handler,"laon_token","sadsadsfdgt")
            setattr(Handler,prop,value)


