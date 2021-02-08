"""审核项目"""
from jsonpath import jsonpath
import pytest
import requests
import json
from middleware.handler import Handler
data=Handler.excel.read_dict("audit")

@pytest.mark.parametrize("info",data)
def test_audit(info,admin_login,add_loan):
    """审核接口"""
    # 添加admin token 放到headers
    headers = json.loads(info["headers"])
    headers["Authorization"] = admin_login["token"]
    # 数据替换，json与eval的区别：如果excel中有true，eval不能转换
    if "#loan_id#" in info["json"]:
        info["json"] = info["json"].replace("#loan_id#",str(add_loan))
    if "#wrong_loan_id#" in info["json"]:
        info["json"] = info["json"].replace("#wrong_loan_id#", str(add_loan+100))
    res = requests.request(method=info["method"],
                           url=Handler.yaml_config["host"] + info["url"],
                           headers=headers,
                           json=json.loads(info["json"]))
    res_json = res.json()

    expected = json.loads(info['expected'])

    # 第一版多值断言
    """
     assert res_json["code"] == expected["code"]
     assert res_json['msg'] == expected['msg']
    """
    # 第二版多值断言
    """    
    for key,value in expected.items():
        # ("code",0)
        assert res_json[key] == value
    """


    # 第三版多值断言
    for key,value in expected.items():
        # 实际结果的value 怎么获取
        jsonpath(res_json,key)[0] == value