import json

import pytest
import requests


from middleware.handler import Handler

data = Handler.excel.read_dict("add")

@pytest.mark.parametrize("info",data)
def test_add(info,login,db):
    if "#member_id#" in info["json"]:
        info["json"] = info["json"].replace("#member_id#",str(login["id"]))
    if "#member_id#" in info["json"]:
        info["json"] = info["json"].replace("#member_id#",str(login["id"]+10))

    res = requests.request(method=info['method'],
                     url=Handler.yaml_config['host'] + info["url"],
                     headers=json.loads(info["headers"]),
                     json=json.loads(info['json']))


    res_body = res.json()

    assert res_body["code"] == info["expected"]
