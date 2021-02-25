from jsonpath import jsonpath
import pytest
import requests
import json
from middleware.handler import Handler
data=Handler.excel.read_dict("invest")

@pytest.mark.parametrize('info',data)
def test_invest(info):
    all_data = json.dumps(info)
    # 替换
    info = Handler.replace_data(all_data)
    print(info)
    # 转化成字典
    info = json.loads(info)
    res = requests.request(method=info['method'],
                           url= Handler.yaml_config['host'] + info['url'],
                           headers = json.loads(info['headers']),
                           json = json.loads(info['json']))
    print(res.json())
    assert res.json()['code'] == info['expected']

    # 设置Handler对应的属性
    if info['extractor']:
        extrators = json.loads(info['extractor'])
        for prop,jsonpath_exp in extrators.items():
            # value = 'token'
            value = jsonpath(res.json(),jsonpath_exp)[0]
            # setattr(Handler,"laon_token","sadsadsfdgt")
            setattr(Handler,prop,value)


