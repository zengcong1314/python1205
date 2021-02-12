import json
import pytest
import requests
from middleware.handler import Handler

data = Handler.excel.read_dict("add")
@pytest.mark.parametrize("info",data)
def test_add_loan(info,loan_login,db):

    if "#member_id#" in info["json"]:
        print(str(loan_login["id"]))
        info["json"] = info["json"].replace("#member_id#",str(loan_login["id"]))
    if "#wrong_member_id#" in info["json"]:
        info["json"] = info["json"].replace("#wrong_member_id#",str(loan_login["id"]+10))
    headers = json.loads(info["headers"])
    headers['Authorization'] = loan_login['token']
    res = requests.request(method=info['method'],
                     url=Handler.yaml_config['host'] + info["url"],
                     headers=headers,
                     json=json.loads(info['json']))
    res_body = res.json()
    assert res_body["code"] == info["expected"]
